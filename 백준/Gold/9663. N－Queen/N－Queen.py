def solveNQueens(n):
    count = 0  # 가능한 해답 개수를 저장하는 변수

    cols = [False] * n         # 각 열에 퀸이 있는지 확인
    diag1 = [False] * (2 * n)  # 좌하향 대각선 (row + col)
    diag2 = [False] * (2 * n)  # 우하향 대각선 (row - col + n)

    def backtrack(row):
        nonlocal count
        if row == n:  # 모든 행에 퀸을 배치했다면 해결된 것
            count += 1
            return

        for col in range(n):
            if cols[col] or diag1[row + col] or diag2[row - col + n]:
                continue  # 해당 위치가 공격 가능하면 스킵

            # 퀸 배치
            cols[col] = diag1[row + col] = diag2[row - col + n] = True

            backtrack(row + 1)  # 다음 행 탐색

            # 백트래킹 (되돌리기)
            cols[col] = diag1[row + col] = diag2[row - col + n] = False

    backtrack(0)
    return count  # 가능한 경우의 수 반환

# 실행 예제
n = int(input())
print(solveNQueens(n))
