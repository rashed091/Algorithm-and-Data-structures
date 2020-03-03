def search(A, x):
    for i in A:
        if i == x:
            return True
    return False

if __name__ == "__main__":
    print(search([2, 3, 6, 8, 9, 11], 6))