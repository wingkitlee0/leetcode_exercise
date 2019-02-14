class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        a = []
        level = 0
        score = [0]
        for i, s in enumerate(S):
            if s == '(':
                level += 1
                a.append(level)
                print(i, s, level)
                if len(score) < level:
                    score.append(0)
            elif s == ')':
                level = a.pop() - 1
                
                if S[i-1]=='(':
                    score[-1] += 1
                else:
                    score[level] += 2*score.pop()
                print(i, s, level, score)
        return score.pop()

if __name__=='__main__':
    S = "((()(())()))"

    sol = Solution()
    print(sol.scoreOfParentheses(S))