class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s == ""):
            return True
        alp ="abcdefghijklmonpqrstuvwxyz0123456789"
        alp = list(alp)
        s = "".join(c.lower() for c in s if c.lower() in alp)
        s = list(s)
        print(s)
        l = len(s)%2
        if(l == 0):
            while len(s) > 0:
                if (s[0].lower() == s[len(s)-1].lower()):
                    s.pop(len(s)-1)
                    s.pop(0)
                else:
                    return False
        else:
            while len(s) > 1:
                if (s[0].lower() == s[len(s)-1].lower()):
                    s.pop(len(s)-1)
                    s.pop(0)
                else:
                    return False
        return True
