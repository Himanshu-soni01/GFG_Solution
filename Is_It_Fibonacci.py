class Solution():
    def solve(self, N, K, GeekNum):
        if N==K or K==1:
            return GeekNum[-1]
        sum = 0
        for i in range(K):
            sum += GeekNum[i]
        GeekNum.append(sum)
        for i in range(N-K-1):
            sum = sum - GeekNum[i] + GeekNum[-1]
            GeekNum.append(sum)
        return GeekNum[-1]

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K = map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N,K,GeekNum))