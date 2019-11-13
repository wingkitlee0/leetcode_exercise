class Tree:
    def __init__(self, x):
        self.val = x
        self.children = []
    
    @staticmethod
    def buildfromrange(N):

        tree = Tree(None)
        curr = tree
        for i in range(1, N+1):
            x = str(i)
            if len(x) == 1:
                curr.children.append(Tree(i))

        return tree
        




class Solution:
    def print(self, tree):

        def dfs(tree):
            if tree is None:
                return
            
            print(tree.val)
            if tree.children is not None:
                for c in tree.children:
                    dfs(c)

        dfs(tree)

    def print_(self, tree):

        stack = [tree]

        while stack:
            curr = stack.pop()

            print(curr.val)
            if curr.children is not None:
                for c in curr.children[::-1]:
                    stack.append(c)
        
    def findKthNumber(self, n: int, k: int) -> int:
        return 0


if __name__ == "__main__":

    tree = Tree.buildfromrange(10)
    #tree.children = [Tree(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    tree.children[0].children = [Tree(x) for x in [10, 11, 12, 13]]



    sol = Solution()
    sol.print_(tree)

