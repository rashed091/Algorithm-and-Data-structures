def fibonacci(n):
    F = [0] * n
    F[1] = 1

    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]

    return F[n - 1]


if __name__ == "__main__":
    print(fibonacci(7))


