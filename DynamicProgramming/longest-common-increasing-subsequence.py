def answer(A, B):
    l1 = len(A)
    l2 = len(B)
    dp = [0] * l2

    for i in range(l1):
        current = 0
        for j in range(l2):
            if A[i] == B[j]:
                dp[j] = max(current + 1, dp[j])
            if A[i] > B[j]:
                current = max(current, dp[j])

    return max(dp)

if __name__ == "__main__":
    a1 = [2, 4, 9, 1]
    a2 = [2, 5, 8, 4, 9, 0, 1]
    print("Length of LCIS is :", answer(a1, a2))
