words = input().split()

special = []
result = []

for word in words:
    w = sorted(word)
    if w not in result:
        result.append(w)
        special.append(word)

print(' '.join(special))