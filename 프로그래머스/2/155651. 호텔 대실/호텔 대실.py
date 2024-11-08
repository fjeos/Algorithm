from collections import defaultdict
def solution(book_time):
    answer = 0
    rooms = defaultdict(tuple)
    books = [[] for _ in range(len(book_time))]
    
    for i in range(len(book_time)):
        info = book_time[i]
        books[i] = [(tuple(map(int, info[0].split(":")))), (tuple(map(int, info[1].split(":"))))]
    books.sort()
    
    number = 0
    for start, end in books:
        assigned = False
        
        for key, value in rooms.items():
            # 이미 존재하는 방에 들어갈 수 있으면
            next_start_time = value[0]
            next_end_time = value[1] + 10
            if next_end_time // 60 == 1:
                next_start_time += 1
                next_end_time %= 60
            if start[0] > next_start_time or (start[0] == next_start_time and start[1] >= next_end_time):
                rooms[key] = end
                assigned = True
                break
        if not assigned:
            rooms[number] = end
            number += 1
            
    return len(rooms)