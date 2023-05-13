from typing import List
class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        res=0
        l=0
        for i in range(n):
            if arr[i]==0:
                if l!=0:
                    res+=1
                    l=0
            else:
                l+=1
        if l==n:
            return -1
        if l!=0:
            res+=1
        return res
