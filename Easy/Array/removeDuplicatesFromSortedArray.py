class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for x in range(0, len(nums)):
            if(x == len(nums)-1):
                nums[index] = nums[x]
                index += 1
                return len(nums[:index:])

            if(nums[x+1] != nums[x]):
                nums[index] = nums[x]
                index += 1
