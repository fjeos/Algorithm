rounds = int(input())
for _ in range(int(input())):
    M, N = map(int, input().split())
    rest_rounds = rounds - max(M, N)
    diff = abs(M - N)
    # 영희와 동수의 점수가 같을 때
    if M == N:
        print(1)
        continue
    # 영희의 점수가 동수보다 클 때
    elif M > N:
        if diff - rest_rounds <= 2:
            print(1)
            continue
    # 동수의 점수가 영희보다 클 때
    elif M < N:
        if diff - rest_rounds <= 1:
            print(1)
            continue
    print(0)