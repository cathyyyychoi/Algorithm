bingolist = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
bingo = 0
reduclist = []

while (bingo != 1):
    row_flag = 0
    col_flag = 0
    cross_left = 0
    cross_right = 0

    userinput = int(input())

    if userinput <= 0 or userinput > 25:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        continue

    elif reduclist.count(userinput) > 0:
        print("중복값을 입력하였습니다. 다시 입력해주세요." )

    else:
        reduclist.append(userinput)
        for i in range(0, 5):
            for j in range(0, 5):
                if userinput == bingolist[i][j]:
                    bingolist[i][j] = 0


        for i in range(0,5):
            row_flag = 0
            col_flag = 0
            for j in range(0, 5):
                if bingolist[i][j] == 0:
                    row_flag = row_flag + 1

                if bingolist[j][i] == 0:
                    col_flag = col_flag + 1

            if row_flag == 5 or col_flag == 5:
                bingo = 1
                break

            if bingolist[i][i] == 0:
                cross_left = cross_left + 1
            if bingolist[5-1-i][i] == 0:
                cross_right = cross_right + 1

        if cross_left == 5 or cross_right == 5:
            bingo = 1
            break

print("Bingo")
			
