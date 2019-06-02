class Solution:
    def twoSum(self, nums, target):
        return self.twoSum_twopass(nums, target)

    def twoSum_twopass_1(self, nums, target):
        """
        two pass implementation

        problem:
            every pair is duplicated
        """

        ht = {}
        result = []
        for i, x in enumerate(nums):
            if x not in ht:
                ht[x] = [i]
            else:
                ht[x].append(i)

        for i, x in enumerate(nums):
            y = target - x

            if y==x:
                if len(ht[x])>=2: # unique pair only
                    result.append([x,x])
                continue

            if y in ht:
                print(x, y)
                result.append([x,y])

        return result

    def twoSum_twopass(self, nums, target):
        """
        two pass implementation

        problem:
            every pair is duplicated
        """

        ht = {}
        result = set()
        for i, x in enumerate(nums):
            if x not in ht:
                ht[x] = [i]
            else:
                ht[x].append(i)

        for i, x in enumerate(nums):
            y = target - x
            
            if y==x:
                if len(ht[x])>=2: # unique pair only
                    result.add(tuple(sorted((x,x))))
                continue

            if y in ht:
                print(x, y)
                result.add(tuple(sorted((x,y))))

        return [list(l) for l in result]

    def twoSum_onepass(self, nums, target):
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
                ht[x].append(i)

            if y in ht:
                # unique pairs only
                result.add(tuple(sorted((x,y))))
                #result.append(sorted([x,y])) 

        return [list(l) for l in result]



if __name__ == '__main__':
    nums = [-1, 0, 1, 0, 2, -2]
    target = 0
    
    sol = Solution()
    result = sol.twoSum(nums,target)
    print(result)

    result = sol.twoSum_onepass(nums,target)
    print(result)

