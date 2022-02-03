import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

new_arr = list(sorted(set(arr))) # 중복된 값 제거
dic = {new_arr[i]:i for i in range(len(new_arr))} # 딕셔너리 형태
# {-10:0, -9:1, 2:2, 4:3}
# value값을 return 

for i in arr:
  print(dic[i], end = ' ')
         
