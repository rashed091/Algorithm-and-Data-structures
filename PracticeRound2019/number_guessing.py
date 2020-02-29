from random import randint

T = int(input())
for _ in range(T):
    A, B = tuple(map(lambda x: int(x), input().split()))
    A = A + 1
    N = int(input())
    judge = ''
    for _ in range(N):
        guess = (A + B) // 2
        print(guess)
        judge = input()
        if judge == 'TOO_SMALL': 
            A = guess + 1
        elif judge == 'TOO_BIG':
            B = guess - 1
        elif judge == 'CORRECT':
            break
        elif judge == 'WRONG_ANSWER':
            break
    if judge == 'WRONG_ANSWER':
        break
