class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for x in range(0, len_s//2):
                temp = s[x]
                s[x] = s[len_s-1-x]
                s[len_s-1-x] = temp       
