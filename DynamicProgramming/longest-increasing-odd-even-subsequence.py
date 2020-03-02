def answer(A):
    n = len(A)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and (A[i] + A[j]) % 2 != 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    print(dp)
    return max(dp)

if __name__ == "__main__":
    A = [2, 7, 3, 4, 9, 1]
    print(answer(A))
