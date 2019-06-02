"""
three-sum problem:
"""
class Solution:
    """
    three-sum problem:
    Given a target (int), find the triplets in an array 
    such that the sum equals to the target.
    """

    def three_sum(self, nums, target):
        """two sum
        """
        return self.three_sum_1(nums, target)

    def three_sum_1(self, nums, target):
        """
        3sum, first try

        x+y+z = target => y+z = w = target-x
        """
        nums = sorted(nums) # O(n log n)
        print("sorted nums = {}".format(nums))
        N = len(nums)

        res = set()
        for i, x in enumerate(nums):
            # make sure j is not repeating
            # made use of sorted nums
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            w = target - x
            print("w = {}".format(w))
            start = i+1
            end = N - 1
            while end > start and nums[start]+nums[end] != w:
                if nums[start]+nums[end] > w:
                    end -= 1
                if nums[start]+nums[end] < w:
                    start += 1
                

                print(start, end, nums[start], nums[end])
            
            if end > start and nums[start]+nums[end] == w:
                res.add(tuple(sorted([nums[start],nums[end],x])))

        return [list(l) for l in res]


    @staticmethod
    def two_sum_onepass(nums, target):
        """
        one pass implementation

        return unique pairs only, e.g.,
        [0,0] returns [0,0] once
        """

        ht = {}
        result = set()
        #result = []
        for i, x in enumerate(nums):
            y = target - x

            if x not in ht:
                ht[x] = [i]
            else:
                # not super important as index is not needed in the current problem
                ht[x].append(i)

            if y in ht:
                # unique pairs only
                result.add(tuple(sorted((x, y))))
                # result.append(sorted([x,y]))

        return [list(l) for l in result]

    

def main():
    """main routine
    """
    args = {'nums' : [-1, 0, 1, 0, 2, -2, 0],
            'target' : 0}

    sol = Solution()
    print(sol.three_sum(**args))


if __name__ == '__main__':
    main()
