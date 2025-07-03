lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

avg_lst  = sum(lst) // len(lst)

greater_avg = [digit for digit in lst if digit > avg_lst]

print(greater_avg)