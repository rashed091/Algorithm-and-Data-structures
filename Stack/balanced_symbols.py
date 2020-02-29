PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            symbol = stack.pop()
        except IndexError:
            return False
        if s != PAIRINGS[symbol]:
            return False
    return len(stack) == 0

print(is_balanced('{[()]})'))

