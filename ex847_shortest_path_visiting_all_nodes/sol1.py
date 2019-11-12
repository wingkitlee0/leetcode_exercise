from collections import defaultdict
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        paths = {}
        npaths = defaultdict(int)
        num_connection = defaultdict(list)
        for i, p in enumerate(graph):
            paths[i] = p
            npaths[i] = len(p)
            num_connection[len(p)].append(i)


        print("paths: ", paths)
        print("num_connection: ", num_connection)
        order = sorted([x for x in num_connection.keys()])
        print(order)

        queue = [(0, [start]) for start in num_connection[order[0]]]
        
        while queue != []:
            k, curr = queue.pop(0)
            visited = set(curr)
            print(visited)
            print("step, curr = {}, {}".format(k, curr))
            if len(visited) == n:
                break
           
            for x in paths[curr[-1]]:
                if npaths[x] >= 1:
                    queue.append( (k+1, curr+[x]))

        return k



if __name__ == '__main__':
    sol = Solution()

    input_list = [
         [[1,2,3],[0],[0],[0]],
         [[1],[0,2,4],[1,3,4],[2],[1,2]]
    ]

    for inp in input_list:
        result = sol.shortestPathLength(inp)
        print(result)