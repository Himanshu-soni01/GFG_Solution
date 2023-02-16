class Solution:
    def solve(self,k,n,arr,dp):
        if k>=n or k<0:
            return 1
        if dp[k]!=-1:
            return dp[k]
        dp[k]=0
        dp[k]=self.solve(k+arr[k],n,arr,dp)
        return dp[k]
        
    def goodStones(self, n, arr) -> int:
        dp=[-1]*(n)
        for i in range(n):
            self.solve(i,n,arr,dp)
        return sum(dp)

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        obj = Solution()
        print(obj.goodStones(n,arr))