class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0 #initialise num_zeroes to equal 0
        n = len(nums)
        for z in range(0, n):
            if(nums[z] == 0):
                num_zeroes += 1

        for x in range(0, n-num_zeroes):
            if(nums[x] == 0):
                for y in range(x+1, len(nums)):
                    if(nums[y] != 0):
                        temp = nums[x]
                        nums[x] = nums[y]
                        nums[y] = temp
                        break
