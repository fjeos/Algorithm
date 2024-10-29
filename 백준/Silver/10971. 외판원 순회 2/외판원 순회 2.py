import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict


def has_visited(cities, now):
    return cities & (1 << now)


def check_visiting(cities, next_city):
    return cities | (1 << next_city)


def tsp(now, visited):
    if visited == (1 << N) - 1:
        return routes[now][0] if routes[now][0] != 0 else 1e9
    if dic[(now, visited)] != 0:
        return dic[(now, visited)]

    answer = 1e9
    for next_city in range(1, N):
        if (not has_visited(visited, next_city)) and (routes[now][next_city] != 0):
            answer = min(answer, (routes[now][next_city] + tsp(next_city, check_visiting(visited, next_city))))
        dic[(now, visited)] = answer
    return answer


N = int(input())
routes = [list(map(int, input().split())) for _ in range(N)]
has_visited(1, 0)
dic = defaultdict(int)
print(tsp(0, 1))
