while True:
    n = int(input())
    if n == -1:
        break

    divisor = [i for i in range(1, n) if n % i == 0]
    print(f"{n} = {' + '.join(map(str, divisor))}" if sum(divisor) == n else f"{n} is NOT perfect.")
