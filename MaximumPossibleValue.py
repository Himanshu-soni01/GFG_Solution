class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        min_ = 10**5
        count_s=0
        total=0
        for i in range(N):
            if B[i]%2==1:
                B[i]-=1
            if B[i]>=2:
                min_ = min(min_,A[i])
            count_s += B[i]
            total += (B[i]*A[i])
        if count_s%4!=0:
            total -= (2*min_)
        return total
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int,input().strip().split()))
        B = list(map(int,input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N,A,B)
        print(ans)