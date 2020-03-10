def subset(S, n):
    m = len(S)
    table = [[False for _ in range(n + 1)] for _ in range(m)]
    for i in range(m):
        table[i][0] = True

    for i in range(m):
        for j in range(n + 1):
            if j < S[i]:
                continue
            if j >= S[i]:
                table[i][j] = table[i][j - S[i]] or table[i - 1][j - S[i]]

    for i in range(m):
        print(table[i][:])

if __name__ == "__main__":
    S = [3, 4, 5, 2]
    n = 9
    subset(S, n)