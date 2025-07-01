n = int(input())

max_seq = 0
curr_seq = 0

lst = [int(input()) for _ in range(n)]

for i in range(1,n):
    if lst[i] > lst[i - 1]:
        curr_seq += 1

        if curr_seq > max_seq:
            max_seq = curr_seq

    else:
        curr_seq= 1

print(max_seq)