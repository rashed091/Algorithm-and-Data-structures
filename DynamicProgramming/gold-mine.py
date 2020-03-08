def gold_coin(gold):
    rows = len(gold)
    cols = len(gold[0])
    cost = [[0 for _ in range(rows)] for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == cols - 1:
                right_up = 0
            else:
                right_up = gold[row - 1][col + 1]

            if col == cols - 1:
                right = 0
            else:
                right = gold[row][col + 1]

            if row == rows - 1 or col == cols - 1:
                right_down = 0
            else:
                right_down = gold[row + 1][col + 1]

            cost[row][col] = gold[row][col] + max(right_up, right, right_down)

    res = 0
    for col in range(cols):
        lst = zip(*cost)[col]
        idx = lst.index(max(lst))
        res += gold[idx][col]

    return res

if __name__ == "__main__":
    # Driver code
    gold = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]

    print(gold_coin(gold))