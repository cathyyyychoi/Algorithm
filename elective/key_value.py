my_set = set()
my_key = ('one', 'two', 'three', 'four', 'five')
my_value = ('일', '이', '삼', '사', '오')

while (True):
    my_input = input()
    if (my_input == 'q'):
        break
    else:
        if my_input in my_key:
            inx = 0
            for i in my_key:
                if my_input == i:
                    break
                inx += 1
            print(my_value[inx])
            break
        else:
            print("NULL")
            break
