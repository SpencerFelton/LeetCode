class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        x = 0
        temp_value_new = 0
        temp_value_prev = 0
        starting_index = 0

        while n < len(nums):
            if(n == 0):
                new_index = (x+k)%len(nums)
                temp_value_prev, nums[new_index] = nums[new_index], nums[x]

                nums[new_index] = nums[x]
                x = new_index
                n += 1
            else:
                new_index = (x+k)%len(nums)
                temp_value_new = nums[new_index]
                nums[new_index] = temp_value_prev
                temp_value_prev = temp_value_new

                x = new_index
                n += 1

                if(x == starting_index):
                    x += 1
                    starting_index = x
                    temp_value_prev = nums[x]
                    
