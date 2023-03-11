def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        freq_ = []
        for i in range(N):
            c=0
            for j in range(i,N):
                if A[i] == A[j]:
                    c+=1
            freq_.append(c)
        res = []
        for i in range(num):
            L = Q[i][0]
            R = Q[i][1]
            k = Q[i][2]
            s=0
            for j in range(L,R+1):
                if freq_[j]==k:
            res.append(s)
        return res
