import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    start = 0
    end = N - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        pivot = A[mid]
        
        if B[i] == pivot:
            found = True
            break
        elif B[i] < pivot:
            end = mid - 1
            mid = (start + end) // 2
            pivot = A[mid]
        elif B[i] > pivot:
            start = mid + 1
            mid = (start + end) // 2
            pivot = A[mid]
        
    print(1 if found else 0)