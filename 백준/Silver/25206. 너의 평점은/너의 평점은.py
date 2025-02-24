dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
sum_sc=0
sum_hak=0
for i in range(20):
    _, hak, score = input().split()
    hak = float(hak)
    if score != 'P':
        sum_sc += (hak * dic[score])
        sum_hak += hak
print("{0:6f}".format(sum_sc/sum_hak))