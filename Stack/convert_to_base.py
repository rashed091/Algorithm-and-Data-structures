DIGITS = '0123456789abcdef'

def convert_to_base(decimal_number, base):
    stack = []
    while decimal_number > 0:
        remainder = decimal_number % base
        stack.append(remainder)
        decimal_number = decimal_number // base
    base_stack = []
    while stack:
        base_stack.append(DIGITS[stack.pop()])

    return ''.join(base_stack)

print(convert_to_base(25, 2))
print(convert_to_base(25, 16))