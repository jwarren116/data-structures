

class Parenthentic(object):

    def isequal(self, text):
        count = 0
        for par in text:
            if par == '(':
                count += 1
            if par == ')':
                count -= 1
                return count
        return count
