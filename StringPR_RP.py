class Solution:
    def solve (self, X, Y, S):
        #code here
        s1 = 'pr'
        s2 = 'rp'
        
        if (X<Y):
            X,Y = Y,X
            s1,s2 = s2,s1
        
        amt = 0
        stack = []
        for i in range(len(S)-1,-1,-1):
            print("1 : ",stack)
            c = S[i]
            f_ = s1[0]
            s_ = s1[1]
            if len(stack)>0 and c==f_ and stack[-1]==s_:
                stack.pop()
                amt += X
            else:
                stack.append(c)
                
        S = ""
        while len(stack)>0:
            S += stack[-1]
            stack.pop()
            
        for i in range(len(S)-1,-1,-1):
            print(S)
            c = S[i]
            f_ = s2[0]
            s_ = s2[1]
            if len(stack)>0 and c==f_ and stack[-1]==s_:
                stack.pop()
                amt += Y
            else:
                stack.append(c)
        return amt
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        ob = Solution()
        print(ob.solve(X,Y,S))


#         10 20
# lrrfrrprgprpppppmurr