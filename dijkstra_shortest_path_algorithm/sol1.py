from typing import Dict, List, Tuple, DefaultDict
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, adj_list: Dict[str, List[str]], distances: Dict[Tuple[str, str], int]):
        self.graph = {}

        for key, neighbors in adj_list.items():
            for neighbor in neighbors:
                t = (key, neighbor) if key < neighbor else (neighbor, key)
                dist = distances[t]
                if key in self.graph:
                    self.graph[key][neighbor] = dist
                else:
                    self.graph[key] = {neighbor: dist}
                if neighbor in self.graph:
                    self.graph[neighbor][key] = dist
                else:
                    self.graph[neighbor] = {key: dist}

class Solution:

    def shortestPath(self, graph: Dict[str, Dict[str, int]], start: str, end: str) -> int:
        """
        Dijkstra's shortest path algorithm

        Note:
        - it uses a min-heap to get the min in O(1) time. However, when a shorter path is computed
          we simply push it to the queue while longer path may be present. Maybe that can be optimized..
        """


        shortest = {vertex: (float('inf'), None) for vertex in graph.keys()} # a table of current shortest paths
        shortest[start] = (0, None)
        seen, unseen = set(), set(graph.keys())

        queue = [(0, start)]
        while queue:
            print(f"curr queue = {queue}")
            print(f"seen = {seen}")
            print(f"shortest = {shortest}")
            curr_dist, curr = heapq.heappop(queue)
            if curr in seen: continue
            
            print(curr, curr_dist)
            for neighbor, dist in graph[curr].items():
                # new distance via curr
                if neighbor in seen: continue
                new_dist = curr_dist + dist
                if new_dist < shortest[neighbor][0]:
                    shortest[neighbor] = (new_dist, curr)
                    heapq.heappush(queue, (new_dist, neighbor))
                    print("added: ", (new_dist, neighbor))
        
            seen.add(curr)
            if end in seen:
                break
            
        return shortest[end][0]


def main():
    input_list = [
        ({'a': ['b', 'd'], 'b': ['a','c','d'], 'c': ['b','e'], 'd': ['a', 'e'], 'e': ['b', 'c', 'd']},
            {('a','b'): 6, ('a','d'): 1, ('b', 'c'): 5, ('b', 'd'): 2, ('b', 'e'): 2, ('c', 'e'): 5, ('d', 'e'): 1},
            'a', 'c'),
        ({'a': ['b', 'c', 'd'], 'b': ['a', 'c', 'f'], 'c': ['a', 'b', 'd', 'f'], 'd': ['a', 'c', 'e', 'g'],
          'e': ['d', 'g', 'h', 'f'], 'f': ['b', 'c', 'e', 'h'], 'g': ['d', 'e', 'h'], 'h': ['e', 'f', 'g']},
            {('a', 'b'): 3, ('a', 'c'): 4, ('a', 'd'): 7, ('b', 'c'): 1, ('b', 'f'): 5, ('c', 'd'): 2,
             ('c', 'f'): 6, ('d', 'e'): 3, ('d', 'g'): 6, ('e', 'f'): 1, ('e', 'g'): 3, ('e', 'h'): 4,
             ('f', 'h'): 8, ('g', 'h'): 2},
             'a', 'h')
    ]

    sol = Solution()
    for inp in input_list:
        graph = Graph(adj_list=inp[0], distances=inp[1])
        for k, v in graph.graph.items():
            print(k, v)

        result = sol.shortestPath(graph.graph, inp[2], inp[3])
        print(result)

if __name__ == "__main__":
    main()
    