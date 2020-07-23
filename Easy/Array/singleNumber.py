class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        for vals in dict:
            if dict[vals] == 1:
                return vals
