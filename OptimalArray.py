def optimalArray(self, n : int, a : List[int]) -> List[int]:
    arr=[0]
    for i in range(1,n):
        arr.append(arr[i-1]+(a[i]-a[i//2]))
    return arr
        
