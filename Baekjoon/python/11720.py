A=int(input())
B=input()
listnum=[]
sum=0
for i in range(A):
    listnum.append(int(B[i]))
for nums in listnum:
    sum+=nums
print(sum)
