def is_prime(n):
    return n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))

lst = [1,15,2,8,31,5,9]

prime_lst = [digit for digit in lst if is_prime(digit)]

print(prime_lst)