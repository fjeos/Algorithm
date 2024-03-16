def solution(park, routes):
    H = len(park)-1
    W = len(park[0])-1
    for i in range(H):
        if 'S' in park[i]:
            current_x = i
            current_y = park[i].index('S')
        
    for route in routes:
        command, time = route.split()
        time = int(time)
        
        movedX = current_x
        movedY = current_y

        for _ in range(time):
            if command == 'E':
                movedY += 1
                if movedY > W or park[current_x][movedY] == 'X':
                    movedY = current_y
                    break

            elif command == 'W':
                movedY -= 1
                if movedY < 0 or park[current_x][movedY] == 'X':
                    movedY = current_y  
                    break

            elif command == 'S':
                movedX += 1
                if movedX > H or park[movedX][current_y] == 'X':
                    movedX = current_x
                    break

            elif command == 'N':
                movedX -= 1
                if movedX < 0 or park[movedX][current_y] == 'X':
                    movedX = current_x
                    break
        current_x = movedX
        current_y = movedY
                
    answer = [current_x, current_y]
    return answer