list2 = [[12,23,2,10,3], [16,8,12,2,1], [23,4,52,33,2], [12,11,6,2,84], [1,2,3,4,5]]
total1 = 0
total2 = 0
for i in range(0, 5):
	total1 = total1 + list2[i][i]
	total2 = total2 + list2[5-1-i][i]

print(total1 - total2)
