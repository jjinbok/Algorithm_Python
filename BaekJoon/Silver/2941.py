croatia = input()
patterns = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for pattern in patterns:
    croatia = croatia.replace(pattern, '*')

croatia_len = len(croatia)
print(croatia_len)
