N, kim, im = map(int, input().split())

count = 0

while kim != im:
    kim = (kim+1)//2
    im = (im+1)//2
    count += 1
    

print(count)