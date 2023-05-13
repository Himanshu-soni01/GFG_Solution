from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:        
        count=0
        for i in range(n//2):
            if arr[i]==arr[n-i-1]:
                continue
            else:
                arr[i]=arr[n-1-i]=0
                count+=1
        
        if count>=2:
            if count%2==0:
                return count//2
            else:
                return ((count-1)//2) + 1
        return count
        
