def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        s=set()
        res = [0 for i in range(N)]
        c=0
        for i in range(1,N):
            if A[i-1] not in s:
                c+=1
                s.add(A[i-1])
            res[i] = (-1 * c)
        
        s=set()
        c=0
        
        for i in range(N-2,-1,-1):
            if A[i+1] not in s:
                c+=1
                s.add(A[i+1])
            res[i] = (res[i]+c)
        for i in range(N):
            res[i] = res[i]*(-1)
        return res
                
