class Solution:
    def countSubstring(self, S):
        ans = 0
        for i in range(len(S)):
            l=u=count=0
            for j in range(i,len(S)):
                if ord(S[j])<=90:
                    u+=1
                if ord(S[j])>=97:
                    l+=1
                if l==u:
                    count+=1

            ans += count
        return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)