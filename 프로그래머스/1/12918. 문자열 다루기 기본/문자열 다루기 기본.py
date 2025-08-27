def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            s = int(s)
            s = str(s)
            return True
        except:
            return False
    return False