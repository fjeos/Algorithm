def solution(storey):
    answer = 0
    digits = list(map(int, str(storey)))
    for i in range(len(digits) - 1, -1, -1):
        print("number: ", digits[i])
        
        if digits[i] < 5:
            print("여기")
            answer += digits[i]
        elif i != 0 and digits[i] > 5:
            print("여기네")
            answer += (10 - digits[i])
            digits[i - 1] += 1
        elif i == 0 and digits[i] > 5:
            print("여기5")
            answer += (10 - digits[i])
            answer += 1
        elif i == 0 and digits[i] == 5:
            answer += digits[i]
        elif digits[i] == 5:
            print("여기4")
            if i != 0 and digits[i - 1] != 9 and digits[i - 1] < 5:
                print("여기2")
                answer += digits[i]
            elif i != 0 and digits[i - 1] == 9:
                answer += (10 - digits[i])
                digits.insert(0, 1)
            elif i != 0:
                print("여기3")
                answer += (10 - digits[i])
                digits[i - 1] += 1
            else:
                answer += digits[i]
        print("now answer: ", answer)
    return answer