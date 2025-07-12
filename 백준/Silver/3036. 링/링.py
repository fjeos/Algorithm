from fractions import Fraction

N = int(input())
r = list(map(int, input().split()))
result = []

for i in range(1, N):
    result.append(Fraction(r[i], r[0]))

for i in range(len(result)):
    print("{0}/{1}".format(result[i].denominator, result[i].numerator))