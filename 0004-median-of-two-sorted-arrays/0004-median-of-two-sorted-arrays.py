class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #two array all odd or even -> average
        # one of them is odd -> no need for average
        tar = len(nums1) + len(nums2)
        need = (tar)%2 == 0
        tar = (tar//2) + 1
        ind1 = 0
        ind2 = 0
        count = 0
        cur = 0
        prev = 0 #previous number
        while ind1 < len(nums1) or ind2 < len(nums2):
            count += 1
            if ind2 >= len(nums2):
                prev = cur
                cur = nums1[ind1]
                ind1 += 1
            elif ind1 >= len(nums1):
                prev = cur
                cur = nums2[ind2]
                ind2 += 1
            else:
                if nums1[ind1] < nums2[ind2]:
                    prev = cur
                    cur = nums1[ind1]
                    ind1 += 1
                else:
                    prev = cur
                    cur = nums2[ind2]
                    ind2 += 1
            if count == tar:
                break
        if need:
            return (prev+cur)/2
        else:
            return cur