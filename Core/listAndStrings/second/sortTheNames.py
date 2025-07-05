names = input().split()

sorted_names = [''.join(sorted(name)) for name in names]

sorted_names.sort()

print(' '.join(sorted_names))

