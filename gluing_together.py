from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']
def concatinate(sym1,sym2):
    return sym1+sym2
whoami = reduce(concatinate, whoami)
print(whoami)