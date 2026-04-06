def hvlcs_solver(char_values, A, B):
    rows = len(A) + 1
    cols = len(B) + 1

    dp = [[0] * cols for _ in range(rows)]

    #Fill dp table
    for i in range(1, rows):
        for j in range(1, cols):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + char_values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    #Backtrack
    i, j = rows - 1, cols - 1
    result = []

    while i > 0 and j > 0:
        if A[i - 1] == B[ j -1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return dp[-1][-1], "".join(result)