import sys

input = lambda: sys.stdin.readline().rstrip()


def preorder(root, order):
    order += root
    left, right = dic[root][0], dic[root][1]
    if left != '.':
        order = preorder(left, order)
    if right != '.':
        order = preorder(right, order)
    return order


def inorder(root, order):
    left, right = dic[root][0], dic[root][1]
    if left != '.':
        order = inorder(left, order)
    order += root
    if right != '.':
        order = inorder(right, order)
    return order


def postorder(root, order):
    left, right = dic[root][0], dic[root][1]
    if left != '.':
        order = postorder(left, order)
    if right != '.':
        order = postorder(right, order)
    order += root
    return order


N = int(input())
dic = dict()
for _ in range(N):
    parent, left, right = input().split()
    dic[parent] = [left, right]

print(preorder('A', ''))
print(inorder('A', ''))
print(postorder('A', ''))
