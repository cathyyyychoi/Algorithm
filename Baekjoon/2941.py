cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for i in cro:
    if i in alpha:
        alpha = alpha.replace(i, ' ')
print(len(alpha))
