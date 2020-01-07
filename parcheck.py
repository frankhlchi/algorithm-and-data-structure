from stack import Stack


def match (open, close):
    open_sym = '([{'
    close_sym = ')]}'
    return open_sym.index(open) == close_sym.index(close)


def parChecker(symbol_str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            top = s.pop()
            if not match(top, symbol):
                balanced = False
        index +=1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print (parChecker('()'))
print (parChecker('{[]}'))
print (parChecker('[{[]}'))