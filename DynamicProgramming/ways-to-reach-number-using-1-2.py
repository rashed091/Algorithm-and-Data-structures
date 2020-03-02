def ways(A, n , X):
    if X == 0:
        return 1
    if X < 0: 
        return 0
    if n<= 0 and X >= 1:
        return 0
    return ways(A, n - 1, X) + ways(A, n, X - A[n-1])


def dynamix_ways(X):
    table = [0] * (X + 1)
    table[0] = 1
    for i in range(1, len(table)):
        table[i] += table[i - 1]
    for i in range(2, len(table)):
        table[i] += table[i - 2]
    print(table)

if __name__ == "__main__":
    A = [1, 2]
    # print(ways(A, 2, 10))
    dynamix_ways(6)
