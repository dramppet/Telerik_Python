vowel ='aeiou'

str_lst = ['apple', 'banana', 'cherry', 'date', 'orange']

startVowel = [w for w in str_lst if w[0].lower() in vowel]

print(startVowel)