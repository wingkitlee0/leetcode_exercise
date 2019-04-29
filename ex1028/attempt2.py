
class TreeNode:
    def __init__(self, x):
        self.val = None
        self.left= None
        self.right=None

def printTree(node):
    if node is None:
        pass
        
    printTree(node.left)
    print("{} ".format(node.x))
    printTree(node.right)


class Solution:
    def recoverFromPreorder(self, S):

        if S == "":
            return None
        if len(S) == 1:
            return TreeNode(int(S[0]))
        

        
        d1 = {}  # value as key
        d2 = {} # level as key

        c = ''
        lvl = 0
        plvl = 0
        for s in S:
            
            if s.isdigit():
                

                x = int(s)
                print(lvl, plvl, s, c)

                d1[s] = []
                if lvl in d2:
                    d2[lvl].append(s)
                else:
                    d2[lvl] = [s]


                i = int(s)

                plvl = lvl
                lvl = 0
                c = s # current
            if s == '-':
                lvl += 1


        return d1, d2

                


if __name__ == '__main__':
    string = "1-2--3--4-5--6---7"

    sol = Solution()

    d1, d2 = sol.recoverFromPreorder(string)

    print(d1)
    print(d2)