import sys
input = sys.stdin.readline

queue = []
for _ in range(int(input())):
    command = list(input().split())
    
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        print(-1 if not queue else queue.pop(0))
        
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        print(1 if not queue else 0)
        
    elif command[0] == 'front':
        print(-1 if not queue else queue[0])
        
    elif command[0] == 'back':
        print(-1 if not queue else queue[-1])