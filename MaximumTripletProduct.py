class Solution:
    def maxTripletProduct (self, arr,  n):
        f=s=t=-10**6
        fm=sm=10**6
        for i in range(n):
            if f<=arr[i]:
                t = s
                s = f
                f = arr[i]
            elif s<=arr[i]:
                t = s
                s = arr[i]
            elif t<=arr[i]:
                t = arr[i]
                
            if arr[i]<=fm:
                sm = fm
                fm = arr[i]
            elif arr[i]<=sm:
                sm=arr[i]
        
        return max(f*s*t,fm*sm*f)

import sys
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob  =Solution()
    res = ob.maxTripletProduct(arr,n)
    print(res)
