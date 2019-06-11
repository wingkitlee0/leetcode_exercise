class Graph:

    @staticmethod
    def dfs(MAP, src, seen=None):
        if src is None:
            return None
        if src == "":
            return None

        if seen is None:
            seen = set(src)

        print("seen = {}".format(seen))        

        if src in MAP:
            for node in MAP[src]: # didnt check the type of MAP[src]
                print("{} : {}".format(src, node))
                if node not in seen:
                    #print("current = {}".format(node))
                    seen.add(node)

                    Graph.dfs(MAP, node, seen)

    @staticmethod
    def dfs_prefix(MAP, src, seen=None, result=None, current=None):
        if src is None:
            return None
        if src == "":
            return None
        
        if seen is None:
            seen = set(src)

        if result is None:
            result = [src]

        if current is None:
            current = "" + src

        #print("seen = {}".format(seen))   
        #print(result)
        if src in MAP:
            for node in MAP[src]: # didnt check the type of MAP[src]
                #print("{} : {}".format(src, node))
                if node not in seen:
                    #print("current = {}".format(node))
                    seen.add(node)
                    result.append(current + node)

                    Graph.dfs_prefix(MAP, node, seen, result, current+node)

            
        return result

    @staticmethod
    def bfs_prefix(MAP, src, seen=None, result=None, current=None):
        if src is None:
            return None
        if src == "":
            return None
        
        if seen is None:
            seen = set(src)

        if result is None:
            result = [src]

        if current is None:
            current = "" + src

        if src in MAP:
            for node in MAP[src]: # didnt check the type of MAP[src]
                #print("{} : {}".format(src, node))
                if node not in seen:
                    #print("current = {}".format(node))
                    seen.add(node)
                    result.append(current + node)

                    Graph.dfs_prefix(MAP, node, seen, result, current+node)

            
        return result

def main():
    MAP = {'A' : ['B', 'C', 'D'],
        'B' : ['E', 'F', 'G'],
        'C' : ['H', 'I'],
        'D' : ['J', 'K'],
        'E' : ['L'] }

    #Graph.dfs(MAP, 'A')

    result = Graph.bfs_prefix(MAP, 'A')
    print(result)
    
    



if __name__ == '__main__':
    main()
