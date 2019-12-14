from collections import deque

def is_palindrome(chars):
    char_deque = deque(chars)

    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            return False
    return True

print(is_palindrome('radar'))