def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    lenX = len(wallpaper)
    lenY = len(wallpaper[0])
    #print(lenX, lenY)
    first = True
    for i in range(lenX):
        for j in range(lenY):
            #print(f"hang : wallpaper[{i}][{j}]: {wallpaper[i][j]}")
            if wallpaper[i][j] == '#' and first:
                lux = i
                first = False
            if wallpaper[i][j] == '#':
                rdx = i+1
    first = True
    for j in range(lenY):
        for i in range(lenX):
            #print(f"yeol : wallpaper[{i}][{j}]: {wallpaper[i][j]}")
            if wallpaper[i][j] == '#' and first:
                luy = j
                first = False
            if wallpaper[i][j] == '#':
                rdy = j+1
    answer = [lux, luy, rdx, rdy]
    return answer