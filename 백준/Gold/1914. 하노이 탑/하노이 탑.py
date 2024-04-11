def hannoi(n, from_pos, to_pos, temp_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    #원반 n-1개를 temp_pos로 이동(보조기둥: to_pos)
    hannoi(n - 1, from_pos, temp_pos, to_pos)
    print(from_pos, to_pos)
    #원반 n-1개를 to_pos로 이동(보조기둥: from_pos)
    hannoi(n - 1, temp_pos, to_pos, from_pos)

N = int(input())

#옮기는 횟수는 2^N-1
num = pow(2, N) - 1
print(num)

#N이 20보다 작은 경우에만 이동 순서 출력
if N <= 20:
    hannoi(N, 1, 3, 2)