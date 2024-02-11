import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards = set(cards)
M = int(input())
nums = list(map(int, input().split()))

print(' '.join(map(str, list(map(lambda x:1 if x in cards else 0, nums)))))    