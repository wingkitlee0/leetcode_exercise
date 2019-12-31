from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
       
        n = len(nums)
        # {x: [idx, idx of x-1]}
        ht = {x: [i, i] for i, x in enumerate(nums)}
        
        start = []
        for x, v in ht.items():
            if x-1 in ht:
                # print(f"Found x-1 in the seq! now update ht[idx[{x-1}]]")
                ht[x-1][1] = ht[x][0]
            else:
                start.append(x)

        def get_length(x):
            j = ht[x][1]
            if nums[j] == x: return 1
            l = 2
            while ht[nums[j]][1] != j: # this is the stopping condition
                # print(j, ht[j])
                l += 1
                j = ht[nums[j]][1]
            return l

        print(f"{start}")

        return max([get_length(x) for x in start])

def main():
    input_list = [
        [100, 4, 200, 1, 3, 2], # 4
        [14, 11, 13, 12], # 4
        [],
        [1, 2, 0 ,1], #3
        [0, 0, 1, -1],
        [20, 21, 19],
        [0, -1],
        [0]
    ]

    sol = Solution()

    for inp in input_list:
        result = sol.longestConsecutive(inp)
        print(f"{inp}: {result}")

if __name__ == "__main__":
    main()