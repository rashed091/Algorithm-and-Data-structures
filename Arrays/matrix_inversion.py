T = int(input())
N = int(input())

for _ in range(T):
    A = []
    for _ in range(N):
        B = input()
        A.append(list(map(lambda x: int(x), B.split())))
    count = 0
    for i in range(N):
        for j in range(N):
            for p in range(N):
                for q in range(N):
                    if i <= p and j <= q and A[i][j] > A[p][q]:
                        count += 1

    print('{}'.format(count))
