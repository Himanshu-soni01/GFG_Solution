class Solution():
    def modulo(self, s, m):
        #your code goes here
        b=1
        count_1=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                count_1+=b
            count_1 %= m
            b *= 2
            b %= m
        return count_1
