class Solution:
    def countPaths(self, N):
        if N < 2:
            return 0
        i = 2
        t = 0
        while i <= N:
            t = (t*3) % ((10**9)+7)

            if i % 2 != 0:
                t -= 3
            else:
                t = (t + 3) % ((10**9)+7)
            i += 1
        return t

if __name__ == "__main__":
    t = int(input())

for _ in range(t):
    N = int(input())
    ob = Solution()
    print(ob.countPaths(N))
    