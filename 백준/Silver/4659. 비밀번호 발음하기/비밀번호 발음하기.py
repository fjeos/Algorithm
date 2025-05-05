ja = ['b','c','d','f','g','h','j','k','l','m','n','q','r','s','t','v','w','x','y','z']
mo = ['a','e','i','o','u']
while True:
    s = input()
    acceptable = True
    if s == 'end':
        break
    if 'a' not in s and 'e' not in s and 'i' not in s and 'o' not in s and 'u' not in s:
        acceptable = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] != 'e' and s[i] != 'o':
                acceptable = False
    for i in range(len(s)-2):
        if (s[i] in ja and s[i+1] in ja and s[i+2] in ja) or (s[i] in mo and s[i+1] in mo and s[i+2] in mo):
            acceptable = False
    if acceptable:
        print("<{0}> is acceptable.".format(s))
    else:
        print("<{0}> is not acceptable.".format(s))