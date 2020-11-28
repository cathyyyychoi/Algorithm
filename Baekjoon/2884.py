H,M=map(int, input().split())
result=M-45
if H>=1 and result<0:
    H=H-1
    result=60-abs(result)
elif H==0 and result<0:
    H=23
    result=60-abs(result)

print(H,result)
