def solution(today, terms, privacies):
    answer = []
    for i in range(len(privacies)):
        today_year, today_month, today_day = map(int, today.split('.'))
        date, term = privacies[i].split()
        year, month, day = map(int, date.split('.'))
        
        dic_terms = {}
        for t in terms:
            types, period = t.split()
            dic_terms[types] = int(period)
        
        month += dic_terms[term]
        while month > 12:
            month -= 12
            year += 1
        
        if year < today_year:
            answer.append(i+1)
        elif year == today_year and month < today_month:
            answer.append(i+1)
        elif year == today_year and month == today_month and day <= today_day:
            answer.append(i+1)
        
    return answer