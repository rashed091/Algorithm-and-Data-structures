def bell_number(n):
    bell = [[0 for i in range(n)] for j in range(n)] 
    bell[0][0] = 1

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                bell[i][j] = bell[i-1][i-1]
            else:
                bell[i][j] = bell[i][j-1] + bell[i-1][j-1]

    return bell[n-1][n-1]

if __name__ == "__main__":
    print(bell_number(5))