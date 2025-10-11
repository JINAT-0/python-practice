n=int(input())
accom=0
for _ in range(n):
    p,q=map(int,input().split())
    if q-p>=2:
         accom=accom+1
    else :
         accom=accom+0 
print(accom)             