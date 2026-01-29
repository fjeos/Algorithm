from fractions import Fraction
n, m = input().split(':')
n, m = int(n), int(m)
nm = Fraction(m, n)
print("{0}:{1}".format(nm.denominator, nm.numerator))