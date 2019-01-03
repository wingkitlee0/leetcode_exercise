class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1); n2 = len(nums2)
        isEven = (n1+n2) % 2 ==0
        nmed = int( (n1+n2)/2 )

        result = []
        i = j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i==n1:
            for r in nums2[j:j+nmed-n1+1]:
                result.append(r)
        if j==n2:
            for l in nums1[i:j+nmed-n2+1]:
                result.append(l)
        print(result)

        if n1+n2==1:
            return result[0]
        if isEven:
            return 0.5*(result[nmed-1]+result[nmed])
        else:
            return result[int(nmed)]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2,32,43,53],[3,4,7,8,100]))