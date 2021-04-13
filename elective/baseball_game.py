import random

count = 0 #몇번 시도했나 세어주는 변수
my_list = [2, 5, 6]
count_list = []
array = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while (count < 6): #count가 5까지 될때까지
    if (count == 5):
        print("Inconsistent ball counts. Try again.")
        break
    #10번 이상 시도하면 게임에 진 것

    computer=random.sample(array,3)

    for i in range(count+1):
        if ((computer) in count_list):
            print("Please guess other numbers. ")
            continue

    count_list.append(computer)

    print(computer[0], computer[1],computer[2],": ball count? ")

    ball,strike=input().split()

    if (strike=='3'):
        print("Computer wins")
        break

    elif (strike!='3'):

        count=count+1

    if (strike=="0" and ball=="0"):
        array.remove(computer[0])
        array.remove(computer[1])
        array.remove(computer[2])
