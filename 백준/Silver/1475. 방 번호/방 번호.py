N = list(map(int, input()))
answer = [0] * 10
for i in range(len(N)):
    if N[i] == 6 or N[i] == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[N[i]] += 1
print(max(answer))