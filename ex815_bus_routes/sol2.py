from typing import List
from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:

        stop2route = defaultdict(list, [])

        for i, r in enumerate(routes):
            for stop in r:
                stop2route[stop].append(i)

        stop2remove = []
        for stop, route in stop2route.items():
            if len(route) == 1 and stop != S and stop != T:
                stop2remove.append( (stop, route[0]) )
        for s, r in stop2remove:
            stop2route.pop(s)
            routes[r].remove(s)

        del stop2remove

        print(stop2route)

    

        # initialize the queue with all possible stops from the bus originated from the stop S
        queue = []
#        queue = [ stop for stop in routes[r] for r in stop2route[S] ]
        for r in stop2route[S]:
            queue.extend([ stop for stop in routes[r] if stop != S])
        # keep a record of buses taken
        #taken = set(stop2route[S])
        #
        visited = set([S])

        k = 1       
        while queue:
            print(queue)
            curr = queue.pop(0)
            if curr == T:
                return k
            #visited.add(curr)
            for r in stop2route[curr]:
                #if r not in taken:
                #    queue.extend([(k+1, stop) for stop in routes[r] if stop != curr and stop not in visited])
                queue.extend([stop for stop in routes[r] if stop != curr and stop not in visited])

            k += 1

        return -1

if __name__ == '__main__':
    sol = Solution()

    input_list = [
        {"routes": [[1, 2, 7], [3, 6, 7]], 'S': 1, 'T': 6},
    ]


    for inp in input_list:
        result = sol.numBusesToDestination(**inp)
        print(result)