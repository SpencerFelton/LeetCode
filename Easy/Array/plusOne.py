class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = map(str, digits)
        num = ''.join(num)
        num = int(num)
        num +=1

        num = list(str(num))
        digits = [int(x) for x in num]

        return(digits)
