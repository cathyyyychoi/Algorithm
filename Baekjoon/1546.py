sub = input()

inputnum = input()
score = inputnum.split(" ")

numlist=[]

for i in range(int(sub)):
    numlist.append(int(score[i]))
numlist.sort()
maxscore = numlist[int(sub) - 1]

newlist = []

for i in numlist:
    newnum = i / maxscore * 100
    newlist.append(newnum)

ave = 0
newsum = 0
for j in newlist:
    newsum += j
    
ave = newsum / int(sub)   
print(ave)
