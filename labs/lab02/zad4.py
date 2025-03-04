def is_balanced(expression: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced('()'))  # True
print(is_balanced('())('))  # False
print(is_balanced('({}'))  # False
print(is_balanced('(}'))  # False
print(is_balanced('(]'))  # False
print(is_balanced('[]'))  # True