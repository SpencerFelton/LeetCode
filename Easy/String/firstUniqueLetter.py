class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        idx = 0

        for chars in s:
            if chars in dict:
                dict[chars][0] += 1
            else:
                dict[chars] = [1, idx]
            idx += 1
        for chars in dict:
            if dict[chars][0] == 1:
                return dict[chars][1]
        return -1
        
