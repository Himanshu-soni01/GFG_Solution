class Solution:
    def minimumNumber(self, n, arr):
        ans=0
        for i in range(n):
            ans = self.gcd(ans,arr[i])
        return ans
      
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
      
      
For Input: 
5
2 4 6 5 4
Your Output: 
1
Expected Output: 
1
