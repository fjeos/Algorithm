import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
guitars = []
for _ in range(N):
    guitar, song = input().split()
    song_mask = 0
    for j in range(M):
        if song[j] == 'Y':
            song_mask |= (1 << j)
    guitars.append(song_mask)
max_song = 0
min_guitar = sys.maxsize


def dfs(index, guitar_count, now_songs):
    global max_song, min_guitar
    song_count = bin(now_songs).count('1')
    if song_count > max_song:
        max_song = song_count
        min_guitar = guitar_count
    elif song_count == max_song:
        min_guitar = min(min_guitar, guitar_count)

    if index == N:
        return
    dfs(index + 1, guitar_count, now_songs)
    dfs(index + 1, guitar_count + 1, now_songs | guitars[index])


dfs(0, 0, 0)
if max_song == 0:
    print(-1)
else:
    print(min_guitar)
