class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if(x<0):
            neg = True
        if(x < 10 and x > -10):
            return x
        str_x = str(x)
        str_x = list(str_x)
        print(str_x)
        if(str_x[len(str_x)-1] == '0'):
            str_x = str_x[:len(str_x)-1:]
        rev_list = str_x[1::]
        rev_list.reverse()
        if(neg):
            str_x = str_x[0] + ''.join(rev_list)
        else:
            str_x = ''.join(rev_list) + str_x[0]
        str_x = int(str_x)
        if str_x < -2**31 or str_x > 2**31:
            return 0
        return str_x
