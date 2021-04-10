my_input = input()
my_list = my_input.split()

for i in range(0, len(my_list)):
    my_list[i] = int(my_list[i])
	
my_set = set(my_list)
my_list = list(my_set)

my_list.sort()
lenlist = len(my_list)

for i in (my_list):
    if i != my_list[lenlist - 1]:
        print(i, end=' ' )
    elif i == my_list[lenlist - 1]:
        print(i)
