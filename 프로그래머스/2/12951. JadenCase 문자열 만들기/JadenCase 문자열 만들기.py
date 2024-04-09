def solution(s):
    s = s.lower()
    is_space = False
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            is_space = True
            string += " "
            continue
        if is_space or i == 0:
            if s[i].isalpha():
                string += s[i].replace(s[i], s[i].upper())
                is_space = False
                continue
        string += s[i]
        is_space = False
        
    return string
