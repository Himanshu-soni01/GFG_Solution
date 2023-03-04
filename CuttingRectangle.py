class Solution:
    def minimumSquares(self, L, B):
        # code here
        min_=min(L,B)
        max_=max(L,B)
        
        while max_%min_>0:
            k = max_%min_
            max_ = min_
            min_ = k
            
        return (L*B)//(min_*min_), min_
            

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L,B = [int(x) for x in input().split()]
        ob = Solution()
        N,K = ob.minimumSquares(L,B)
        print(N,end = " ")
        print(K)