N = int(input())
prime = [2, 3, 5, 7]
for i in range(11, 104):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 !=0:
        prime.append(i)
for i in range(len(prime)-1):
    if prime[i] * prime[i+1] > N:
        print(prime[i] * prime[i+1])
        break