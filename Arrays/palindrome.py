
def palindrom(s):
    flag = True
    for i in range(len(s)):
        if s[i] == s[len(s) - i - 1]:
            flag = True
        else:
            return False
    return flag


T = int(input())

for _ in range(T):
    S = input()
    isPalin = 'YES' if palindrom(S) else 'NO'
    isEven = 'EVEN' if len(S) % 2 == 0 else 'ODD'
    if isPalin == 'YES':
        print("{} {}".format(isPalin, isEven))
    else:
        print("{}".format(isPalin))
