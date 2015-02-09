

def isequal(text):
    count = 0
    for par in text:
        if par == '(':
            count += 1
        if par == ')':
            count -= 1
        return count
