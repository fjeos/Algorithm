def solution(sizes):
    long, short = [], []
    for w, h in sizes:
        if w <= h:
            long.append(h)
            short.append(w)
        else:
            long.append(w)
            short.append(h)
            
    return max(long) * max(short)