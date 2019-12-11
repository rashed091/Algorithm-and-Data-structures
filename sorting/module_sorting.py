N, K = tuple(map(int, input().split()))
A = list(map(int, input().split()))

A.sort(key=lambda x: x % K)
print(*A, sep=" ")
