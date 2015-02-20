

def is_balanced(text):
    count = 0
    for char in text:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count == -1:
            return count
    if count > 0:
        return 1
    return count
