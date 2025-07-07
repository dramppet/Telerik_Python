str_word = input()

word = str_word[0]
max_word = 1
curr_word = 1

for w in range(1,len(str_word)):
    if str_word[w] == str_word[w -1]:
        curr_word += 1

        if curr_word > max_word:
            max_word = curr_word
            word = str_word[w]

    else:
        curr_word = 1


print(word * max_word)

