vowel = 'aouei'

n = int(input())
best_food = ''
best_vowel = -1
best_length = -1
best_ratio = float('inf')

while n > 0:
    food = input()
    count_vowel = sum(1 for ch in food if ch in vowel)
    ratio = count_vowel / len(food)

    if (ratio < best_ratio or
            (ratio == best_ratio and count_vowel > best_vowel) or
            (ratio == best_ratio and count_vowel == best_vowel and len(food) > best_length)):
        best_ratio = ratio
        best_food = food
        best_vowel = count_vowel
        best_length = len(food)

    n -= 1

print(f'{best_food} {best_vowel}/{best_length}')
