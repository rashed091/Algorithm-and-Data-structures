def change_count(S, n):
    m = len(S)
    table = [0 for _ in range(n+1)]
    table[0] = 1

    for i in range(m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]


if __name__ == "__main__":
    arr = [1, 2, 3]
    n = 5
    print(change_count(arr, n))
