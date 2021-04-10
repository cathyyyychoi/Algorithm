num_list = []

for i in range(0,5):
    user_input = input()
    num_list.append(user_input)
    #입력받은 숫자를 리스트에 넣어준다.

diff_list = []
minnum = 0
for i in range(0, len(num_list)):
    for j in range(0, len(num_list)):
        diff1 = int(num_list[i]) - int(num_list[j])
        diff_list.append(abs(diff1))
	#리스트의 요소끼리 뺄셈을 하여 새로운 리스트에 넣어준다.

for i in range(0, len(num_list)):
    diff_list.remove(0)
diff_list.sort()
#같은 숫자끼리 빼면 생기는 '0'요소를 없애준다. 그리고 sort시킨다.

minnum=diff_list[0]
#sort시킨 리스트의 첫번째 원소가 최소이다.

print(minnum)
