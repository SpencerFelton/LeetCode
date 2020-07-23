class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for x in range(len(nums1)-1, -1, -1):
            if nums1[x] in nums2:
                intersection.append(nums1[x])
                nums2.pop(nums2.index(nums1[x]))
                nums1.pop(x)

        return(intersection)
    
