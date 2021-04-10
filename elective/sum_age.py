str1=input()
#문자열 입력
num=0
total1=0

for i in range(20,31):
    #나이 범위가 20,30 사이
    
    if str(i) in str1:
        total1 = total1 + int(i) #모든 숫자를 더하고
        if str1.count(str(i)) > 1: #숫자를 세서 1번 이상이면
            total1 = total1 + int(i) * ((str1.count(str(i))) - 1)
            #나온 횟수만큼 더해준다
print(total1)
