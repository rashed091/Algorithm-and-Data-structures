def binomial(n, k):
    if n <= 2:
        return 1

    bin = [[1 for _ in range(n + 1)] for _ in range(n +  1)]

    for i in range(2, n + 1):
        for j in range(i+ 1):
            if j == 0 or j == i:
                continue
            else:
                bin[i][j] = bin[i-1][j-1] + bin[i-1][j]

    return bin[n][k]

if __name__ == "__main__":
    print(binomial(7, 3))