A, B = map(int, input().split())
C = int(input())

if A + (B + C) // 60 > 23:
    A = (A + (B + C) // 60) - 24
else:
    A += (B + C) // 60
print(A, (B + C) % 60)
    
