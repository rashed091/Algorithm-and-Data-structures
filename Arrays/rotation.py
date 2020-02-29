T = int(input())

for _ in range(T):
    B = input()
    N, K = tuple(map(lambda x: int(x), B.split()))
    A = input()
    A = list(map(lambda x: int(x), A.split()))
    K = K if K < N else K % N
    L = A[-K:] + A[:-K]

    print(*L, sep=" ")
