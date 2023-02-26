def findSubArrays(self,arr,n):
  d = {0:1}
  sum=0
  count=0
  for i in range(n):
       sum+=arr[i]
       if sum in d:
           count+=d[sum]
           d[sum]+=1
       else:
           d[sum]=1
  return count
