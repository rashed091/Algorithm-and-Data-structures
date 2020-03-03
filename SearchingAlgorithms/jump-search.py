import math

def jump_search(A, x):
    n = len(A)
    block = int(math.sqrt(n))

    start = 0
    while A[min(block, n)] < x:
        start = block
        block += int(math.sqrt(n))
        if start > n:
            return -1
    


if __name__ == "__main__":
    # Driver code to test function
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
    x = 55
