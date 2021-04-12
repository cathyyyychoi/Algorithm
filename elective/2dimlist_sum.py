list2 = [[1,2,3,10],[6,8,12],[23,4],[11,2,36]]
total = 0
for i in range(0, 4):
	for j in range(0, len(list2[i])):
		item = list2[i][j]
		total = total + item
print(total)
