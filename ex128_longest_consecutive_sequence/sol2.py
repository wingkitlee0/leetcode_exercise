from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        # {i: i}
        ht = {i: i for i, x in enumerate(nums)}
        # {x: i}
        idx = {x: i for i, x in enumerate(nums)}

        seen = set()
        for i, v in ht.items():
            x = nums[i]

        #    print(x, v)
            if x-1 in idx:
                # print(f"Found x-1 in the seq! now update ht[idx[{x-1}]]")
                ht[idx[x-1]] = idx[x]
                seen.add(idx[x])
        #print(f"seen: {seen}")

        def get_length(i):
            j = ht[i]
            if ht[j] == i: return 1
            if ht[j] == j: return 2
            
            l = 2
            while ht[j] != j:
                # print(j, ht[j])
                l += 1
                j = ht[j]
            return l
        #print(f"{ht}")
        lengths = [get_length(i) for i in ht if i not in seen]
        #print(lengths)
        return max(lengths)

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