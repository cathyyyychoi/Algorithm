inputnum = 0
total = 0

while inputnum != 11:
    num1 = int(input())
    
    if num1 != -1:
        total = total + num1
        inputnum = inputnum + 1
	
    elif num1 == -1:
        total = total + num1 + 1
        inputnum = inputnum + 1
        break
		
print(total)
