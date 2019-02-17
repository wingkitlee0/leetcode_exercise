from tree import Tree
from lexicographical import compare

class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n>1 and k>1:
            t = Tree(1, compare=compare)
            count = 1
            tmax = 1
            for l in range(2,n+1):
                if count < k:
                    t.addNode(l)
                    tmax = t.find_max()
                    count += 1
#                    print("# added %i and now max = %i" % (l, tmax))
                else: # count > k

                    if int(str(l)[0])

                    if compare(l, tmax):
                        t.addNode(l)
                        t, tmax = t.del_max()
#                        print("# added %i and removed max. current max = %i" % (l, tmax))
                    else:
                        continue
                    
#            t.printTree()
            return t.find_max()
        else:
            if n==1 or k==1:
                return 1

if __name__=='__main__':
    import sys
    N = int(sys.argv[1])
    k = int(sys.argv[2])

    sol = Solution()

    result = sol.findKthNumber(n=N, k=k)
    print("N, k", N, k)
    print(result)