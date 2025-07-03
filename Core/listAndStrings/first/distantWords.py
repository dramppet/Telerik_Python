target_number = int(input())
count_words = int(input())

words = [input().lower() for _ in range(count_words)]
distance = [abs(sum(ord(c) -96 for c in w) - target_number) for w in words]

for i in range(len(words)):
    print(f'{words[i]} {distance[i]}')

avg_distance  = sum(distance) / count_words

print(f'{avg_distance:.2f}')
