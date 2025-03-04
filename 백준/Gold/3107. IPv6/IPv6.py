import sys


def normalize_ipv6(v6):
    # 특수한 경우: 전체가 0인 경우
    if v6 == '::':
        return '0000:0000:0000:0000:0000:0000:0000:0000'

    # :: 위치 찾기
    if '::' in v6:
        left, right = v6.split('::')
        left_parts = left.split(':') if left else []
        right_parts = right.split(':') if right else []
        # 0으로 채워야 할 그룹 수 계산
        zero_groups = 8 - len(left_parts) - len(right_parts)

        # 완전한 주소 구성
        full_parts = left_parts + ['0000'] * zero_groups + right_parts
    else:
        full_parts = v6.split(':')

    # 각 그룹을 4자리로 패딩
    normalized_parts = [part.zfill(4) for part in full_parts]

    return ':'.join(normalized_parts)


# 입력 받기
v6 = sys.stdin.readline().rstrip()
print(normalize_ipv6(v6))