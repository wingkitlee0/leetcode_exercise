from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        # {x: (next value, max of seq)}
        ht = {i: [i, i] for i in range(n)}
        # {x: i}
        d = {x: i for i, x in enumerate(nums)}

        seen = set()
        for i, v in ht.items():
            print(i, {nums[j]: v for j, v in ht.items()})
            x = nums[i]
            if (x-1) in d:
                print(f"Found {x-1} in d! now update ht[{d[x-1]}]")
                ht[d[x-1]] = [v[0], v[1]]
                seen.add(i)
        print(f"seen: {seen}")
        lengths = [nums[v[1]]-nums[i]+1 for i, v in ht.items() if i not in seen]
        print(lengths)
        return max(lengths)

def main():
    input_list = [
        [100, 4, 200, 1, 3, 2], # 4
        [14, 11, 13, 12], # 4
        [],
        [1, 2, 0 ,1], #3
        [0, 0, 1, -1],
        [20, 21, 19]
    ]

    sol = Solution()

    for inp in input_list:
        result = sol.longestConsecutive(inp)
        print(f"{inp}: {result}")

if __name__ == "__main__":
    main()