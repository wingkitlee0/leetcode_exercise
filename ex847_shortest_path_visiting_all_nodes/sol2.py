from collections import defaultdict, Counter
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        paths = {}
        num_connection = defaultdict(list)
        for i, p in enumerate(graph):
            paths[i] = p
            num_connection[len(p)].append(i)


        print("paths: ", paths)
        print("num_connection: ", num_connection)
        order = sorted([x for x in num_connection.keys()])
        print(order)

        queue = [(0, [start]) for start in num_connection[order[0]]]
        
        step = 0
        while queue != [] :
            #print(queue)
            k, curr = queue.pop(0)
            step += 1
            visited = Counter(curr)
            print("visited: ", visited)
            print("k, curr = {}, {}".format(k, curr))
            if len(visited) == n:
                break
           
            #for x in paths[curr[-1]]:
            next = sorted(paths[curr[-1]], key=lambda x: len(paths[x]))
            #print("next = ", next)
            single_list = []
            while next != [] and len(paths[next[0]]) == 1:
                x = next.pop(0)
                single_list.append(x)

            if single_list:
                tail = []
                for i, x in enumerate(single_list):
                    if visited[x] == 0:
                        if i < len(single_list)-1:
                            tail += [x, curr[-1]]
                        else:
                            tail += [x]
                queue.append( (k+len(tail), curr + tail))

            
            for x in next:
                if not (visited[x] >= 1 and len(paths[x]) == 1):
                    queue.append( (k+1, curr+[x]))
                if len(paths[x]) == 1 and visited[x] == 0:
                    queue.append( (k+2, curr + [x, curr[-1]]) )

        print("step = ", step)
        return k



if __name__ == '__main__':
    sol = Solution()

    input_list = [
         [[1,2,3],[0],[0],[0]],
         [[1],[0,2,4],[1,3,4],[2],[1,2]],
         [[2,5,7],[2,4],[0,1],[5],[5,6,1],[4,10,8,0,3],[4,9],[0],[5],[6],[5]]
    ]

    for inp in input_list:
        result = sol.shortestPathLength(inp)
        print(result)