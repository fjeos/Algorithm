def solution(phone_book):
    answer = True
    phone_book.sort()
    if any(phone_book[i] == phone_book[i+1][:len(phone_book[i])] for i in range(len(phone_book)-1)):
        answer = False
    return answer