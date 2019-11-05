class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nh = len(haystack)
        nn = len(needle)

        if nh == 0 or nn == 0 or nn > nh:
            return 0

        dummy = [False] * nn

        i = 0; j = 0
        while i < nh and j < nn:
            if haystack[i] == needle[j]:
                dummy[j] = True
                i += 1
                j += 1
            else:
                if any(dummy):
                    dummy = [False for _ in range(nn)]
                    j = 0
                i += 1

        print("---")
        print(i, j, dummy)
        
        if j == nn and all(dummy):
            return i-nn
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    
    input_list = [
        {'haystack': "hello", 'needle': "ll"}, 
        {'haystack': "aaaa", 'needle': "bba"},
        {'haystack': "hellolllo", 'needle': "lll"},
        {'haystack': "mississippi", 'needle': "issip"}
    ]

    for inp in input_list:
        result = s=sol.strStr(**inp)
        print(result)


        

