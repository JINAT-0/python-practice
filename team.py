n=int(input())
temp=0
for t in range(n):
    p,v,to=map(int,input().split())

    if p+v+to>=2:
        temp+=1
print(temp)       
