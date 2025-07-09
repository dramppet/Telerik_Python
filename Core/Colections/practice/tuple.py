#task 1
my_tuple = ('Hello',1,1.1)

for el in my_tuple:
    print(el)

print(my_tuple.count(1)) # return тхе count of a specified element
print(my_tuple.index(1.1)) # return index of a specified element

print(10*'- ')

#task 2
my_tuple = ("apple", "banana", "cherry")

second_el = my_tuple[2] # return el from index
print(second_el)

print(10*'- ')

#task 3
my_tuple = (10, 20, 30)

a, b, c = my_tuple  #unpacking my_tuple
d, *f = my_tuple

print(a)
print(b)
print(c)
print(d)
print(f)

print(10*'- ')

#task 4
my_tuple = (1, 2, (3, 4))

print(my_tuple[2][1])