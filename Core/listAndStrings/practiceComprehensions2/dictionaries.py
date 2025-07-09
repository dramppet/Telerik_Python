#task1
print('Character Frequency Counter')

s = "hello"

my_dict = {}

for el in s:
    if el not in  my_dict:
        my_dict[el] = 1
    else:
        my_dict[el] += 1

print(my_dict)

print(50 * '-')

#task 2
import re
print('Tokenize a paragraph and count how many times each word appears.')

import re

text = "Hello, World! Hello, Python, too!"
my_text = re.split(r'[,!\s]+', text)

my_dict = {}

for el in my_text:
    if el:  # skip empty strings
        my_el = el.lower()
        if my_el not in my_dict:
            my_dict[my_el] = 1
        else:
            my_dict[my_el] += 1

print(my_dict)
print(50 * '-')

#task3
print('Inventory System')

inventory = {"apple": 5, "banana": 3}
sales = ["apple", "banana", "apple", "apricot"]

while len(sales) > 0:
    for k, v in inventory.items():
        el = sales.pop(0)
        if el in k:
            inventory[k] -= 1
        else:
            print('Product not available')

print(inventory)
print(50 * '-')

#task 4
print('Nested Dictionaries')

data = {
  "Alice": {"math": 90, "english": 85},
  "Bob": {"math": 78, "english": 88}}

data_dict = {}

evaluation = 0
for k,v in data.items():
    for j,l in v.items():
        evaluation += l
    data_dict[k] = evaluation / 2
    evaluation = 0

print(data_dict)
print(50 * '-')

#task 5
print('Lookup by Value')

d = {"us": "USA", "bg": "Bulgaria", "ca": "Canada"}
target_value = "Bulgaria"

for v in d.values():
    if target_value in v:
        print(f'Target value {target_value} exists: True')

#task 6
print('Merge Two Dictionaries')

a = {"apple": 3, "banana": 1}
b = {"apple": 2, "cherry": 4}

result = {}

for k,v  in a.items():
    result[k] = v

for k,v in b.items():
    if k in result:
        result[k] += v
    else:
        result[k] = v

print(result)

print(50 * '-')

#task 7
print('Sort Dictionary by Value')

d = {"apple": 5, "banana": 2}

my_dict = dict(sorted(d.items(),key = lambda x: -x[1]))

print(my_dict)





