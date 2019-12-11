S = input()
K = int(input())

A = []
for i in range(len(S)):
    A.append(S[i:])

A.sort()
print(A[K-1], sep=" ")
