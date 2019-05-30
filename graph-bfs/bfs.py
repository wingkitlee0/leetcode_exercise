"""
An implementation of BFS presented in Erik Deremaine's MIT class
"""

def BFS(Adj, s='s'):
    level = {s : 0}
    parent = {s : None}
    i = 1

    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    
    return level, parent

if __name__ == '__main__':
    Adj = {
        's' : ['a', 'x'],
        'a' : ['z'],
        'x' : ['s', 'd', 'c'],
        'd' : ['x', 'c', 'f'],
        'c' : ['x', 'd', 'f', 'v'],
        'f' : ['d', 'c', 'v'],
        'v' : ['c', 'f'],
        'z' : ['a']
    }

    level, parent = BFS(Adj, 's')

    level_r = dict()
    for k, v in level.items():
        if v not in level_r:
            level_r[v] = [k]
        else:
            level_r[v].append(k)

    for k, v in level_r.items():
        print(k, v)


    print(level)

    print(parent)

