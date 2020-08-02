class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict_s = {}
        dict_t = {}

        for x in range(0, len(s)):
            if(s[x] in dict_s):
                dict_s[s[x]] += 1
            if(t[x] in dict_t):
                dict_t[t[x]] += 1
            if(s[x] not in dict_s):
                dict_s[s[x]] = 1
            if(t[x] not in dict_t):
                dict_t[t[x]] = 1
        print(dict_s)
        print(dict_t)
        if(dict_s == dict_t):
            return True
        return False
        
