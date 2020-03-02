def answer(n):
    ugly = [0] * n
    ugly[0] = 1
    u2 = u3 = u5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        if ugly[i] == next_multiple_of_2:
            u2 += 1
            next_multiple_of_2 = ugly[u2] * 2
        if ugly[i] == next_multiple_of_3:
            u3 += 1
            next_multiple_of_3 = ugly[u3] * 3
        if ugly[i] == next_multiple_of_5:
            u5 += 1
            next_multiple_of_5 = ugly[u5] * 5
    
    return ugly[-1]

if __name__ == "__main__":
    print(answer(5))