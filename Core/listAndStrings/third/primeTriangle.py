def is_prime(n):
    if n == 1:
        return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())

sequence = []
for num in range(1, N+1):
    if is_prime(num):
        line = ''
        for i in range(1, num+1):
            line += '1' if is_prime(i) else '0'
        print(line)
