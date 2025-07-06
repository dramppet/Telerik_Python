start_pos = int(input())
lst = list(map(int,input().split(',')))

forward_sum = 0
backward_sum = 0
curr_pos = start_pos

while True:
    line = input()

    if line == 'exit':
        break

    step, direction, size = line.split()
    step = int(step)
    size = int(size)

    for _ in range(step):
        if direction == 'forward':
            curr_pos = (curr_pos + size) % len(lst)
            forward_sum += lst[curr_pos]
        elif direction == 'backwards':
            curr_pos = (curr_pos - size) % len(lst)
            backward_sum += lst[curr_pos]

print(f'Forward: {forward_sum}')
print(f'Backwards: {backward_sum}')