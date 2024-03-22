def solution(numbers, hand):
    answer = ''
    keypad = {0: [3, 1], '*': [3, 0], '#': [3, 2]}
    k = 1
    for i in range(4):
        for j in range(3):
            keypad[k] = [i, j]
            k += 1
        if k == 10:
            break
    
    left = keypad['*']
    right = keypad['#']
    for number in numbers:
        x, y = keypad[number]
        if number in [1, 4, 7]:
            answer += 'L'
            left = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right = keypad[number]
        else:
            left_dis = abs(left[0] - keypad[number][0]) + abs(left[1] - keypad[number][1])
            right_dis = abs(right[0] - keypad[number][0]) + abs(right[1] - keypad[number][1])
            if left_dis < right_dis:
                answer += 'L'
                left = keypad[number]
            elif right_dis < left_dis:
                answer += 'R'
                right = keypad[number]
            else:
                if hand == "right":
                    answer += 'R'
                    right = keypad[number]
                else:
                    answer += 'L'
                    left = keypad[number]
                
    return answer
