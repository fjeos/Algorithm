S = []
N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

for i in range(N):
    S.append(A[i]*B[i])

print(sum(S))