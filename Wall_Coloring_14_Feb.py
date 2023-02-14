def minCost(colors, N):
    if N == 0:
        return 0

    # for i in range(3):
    #     dp.append([])
    #     for j in range(3):
    #         dp[i].append(0)]

    dp = [[0 for i in range(3)] for j in range(N)]

    for i in range(3):
        dp[0][i] = colors[0][i]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]

        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]

        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + colors[i][2]

    return min(dp[-1][0], dp[-1][1], dp[-1][2])

if __name__ == "__main__":
    N = 3
    colors = [[14, 2, 11],
             [11, 14, 5],
             [14, 3, 10]]
    N=len(colors)
    print(minCost(colors,N))
