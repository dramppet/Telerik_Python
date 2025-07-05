lst = list(map(int,input().split()))

remainder_zero = []
remainder_one = []
remainder_two = []

for el in lst:
    if el % 3 == 0:
        remainder_zero.append(el)
    elif el % 3 == 1:
        remainder_one.append(el)
    else:
        remainder_two.append(el)

print(*remainder_zero,sep=" ")
print(*remainder_one,sep=" ")
print(*remainder_two,sep=" ")