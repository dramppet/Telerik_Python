# task 1
print('Square Numbers')

my_dict = {el: el * el for el in range(1, 11)}

print(my_dict)
print(50*'-')

# task2
print(f'Filter Even Numbers')

lst = [1, 2, 3, 4, 5]

my_dict = {el: el * el for el in lst if el % 2 == 0}

print(my_dict)
print(50*'-')

# task3
print('Invert a Dictionary')

d = {"a": 1, "b": 2}

my_dict = {v: k for k, v in d.items()}

print(my_dict)
print(50*'-')

# task4
print('Conditional Dictionary')

prices = {"pen": 10, "book": 25, "bag": 50}

my_dict = {k: v for k, v in prices.items() if v >= 25}

print(my_dict)
print(50*'-')

# task5
print('Word Length Mapping')

words = ["hello", "world"]

my_dict = {el: len(el) for el in words}

print(my_dict)
print(50*'-')

# task6
print('Grade Categorization')

grades = {"Alice": 85, "Bob": 55}

my_dict = {k: 'Pass' if v > 60 else 'Fail' for k, v in grades.items()}

print(my_dict)
print(50*'-')

# task 7

s = "banana"

my_dict = {el: s.count(el) for el in set(s)}
print(my_dict)
print(50*'-')