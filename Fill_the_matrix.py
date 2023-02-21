class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        if N*M==1:
            return 0
        ans =0
        for i in range(1,N+1):
            for j in range(1,M+1):
                ans = max(ans,abs(x-i)+abs(y-j))
        return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N,M = map(int,input().split())
        x,y = map(int,input().split())
        ob = Solution()
        print(ob.minIteration(N,M,x,y))