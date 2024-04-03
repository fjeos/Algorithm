from collections import defaultdict
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    answer = 1
    
    alphabet = [chr(i + 97) for i in range(26)]
    dictA, dictB, dictUnion, dictInter = defaultdict(int), defaultdict(int), dict(), dict()
    
    for i in range(1, len(str1)):
        if str1[i-1] in alphabet and str1[i] in alphabet:
            s = (str1[i-1] + str1[i])
            dictA[s] += 1
    for j in range(1, len(str2)):
        if str2[j-1] in alphabet and str2[j] in alphabet:
            s = (str2[j-1] + str2[j])
            dictB[s] += 1

    #if dictA and dictB:
    for i in dictA:
        if i in dictB:
            dictUnion[i] = max(dictA[i], dictB[i])
            dictInter[i] = min(dictA[i], dictB[i])
        else:
            dictUnion[i] = dictA[i]
    for i in dictB:
        if i in dictA:
            dictUnion[i] = max(dictA[i], dictB[i])
            dictInter[i] = min(dictA[i], dictB[i])
        else:
            dictUnion[i] = dictB[i]
    print(dictUnion, dictInter)
    if len(dictInter) == 0 and len(dictUnion) == 0:
        answer = 1
    else:
        answer = sum(dictInter.values()) / sum(dictUnion.values())
    

    return int(answer * 65536)