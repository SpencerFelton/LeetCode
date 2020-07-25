class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            sum_num = target - nums[x]
            for y in range(x+1, len(nums)):
                if (nums[y] == sum_num):
                    return[x, y]
