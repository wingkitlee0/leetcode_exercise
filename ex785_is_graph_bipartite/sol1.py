from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)


        seen = {} # key: value = node: group

        if graph[0] == []:
            queue = [(0, 0)]
        else:
            queue = [(0, 1)] # (node, group), where two groups are 1 or -1

        while queue != []:
            curr, curr_grp = queue.pop(0)
            if curr not in seen:
                seen[curr] = curr_grp
            else:
                if seen[curr] != curr_grp:
                    return False

            print(curr, curr_grp)

            for node in graph[curr]:
                if node not in seen and graph[node] != []:
                    queue.append( (node, -curr_grp))
                else:
                    if seen[node] == curr_grp:
                        return False

        return True

            
if __name__ == "__main__":
    
    input_list = [
        [[1,3], [0,2], [1,3], [0,2]], # true
        [[1,2,3], [0,2], [0,1,3], [0,2]], # false
        [[4,1],[0,2],[1,3],[2,4],[3,0]], # false
        [[2],[3],[0,3],[1,2]], # true
        [[],[3],[],[1],[]], # true
        [[]],
        [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]], # false
    ]

    sol = Solution()

    for graph in input_list:
        result = sol.isBipartite(graph)
        print(result)