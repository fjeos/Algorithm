N = int(input())
count = 0

for A in range(1, N):
    for B in range(A, N):
        C = N - (A + B)
        if C < B:
            break
        if C < A + B:
            count += 1

print(count)