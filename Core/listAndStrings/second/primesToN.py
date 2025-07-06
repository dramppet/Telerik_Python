number = int(input())

def prime(n):
    if n == 1:
        return True
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primeNumber = []

for n in range(number + 1):
    if prime(n):
        primeNumber.append(n)

print(*primeNumber,sep=' ')