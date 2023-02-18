class Solution:
    def appleSequences(self, n, m, arr):
        i=j=0
        count_A = count_m = count = 0
        
        while j<n:
            if arr[j] == "A":
                count_A += 1
            else:
                if count_m<m:
                    count_m += 1
                else:
                    while i < j and arr[i] != 'O':
                        i += 1
                        count_A -=1 
                    i += 1
            
            count = max(count,count_A + count_m)
            j += 1
        return count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N,M,arr))