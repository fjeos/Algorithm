for _ in range(int(input())):
    R, S = map(str, input().split())
    s = ''
    for i in range(len(S)):
        for j in range(int(R)):
            s += S[i]
    print(s)