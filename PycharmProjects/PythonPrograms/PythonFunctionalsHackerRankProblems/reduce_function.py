# def adder(a,b):
#     return a+b
#
# from functools import reduce
# l=[1,2,3,4,5,6]
# print(reduce(adder,l))
# print(reduce(lambda a,b:a+b, l))
#
# from fractions import  Fraction
# p=Fraction(0.625)
# print(p)
# print(p.numerator,p.denominator)

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda a,b:a*b, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)