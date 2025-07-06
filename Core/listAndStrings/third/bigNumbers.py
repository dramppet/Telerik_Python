num = [int(x) for x in input().split()]

first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

max_len = max(len(first),len(second))
result = []
ost = 0

for idx in range(max_len):
    digit1 = first[idx] if idx < len(first) else 0
    digit2 = second[idx] if idx < len(second) else 0

    total = digit1 + digit2 + ost
    result.append(total % 10)
    ost = total // 10

print(*result)
