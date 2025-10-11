n=int(input())
#a,b,c,d=map(int,input().split())

for i in range(n):
    a,b,c,d=map(int,input().split())
    temp=0
    if a<b:
        temp+=1
    if a<c:
        temp+=1
    if a<d:
        temp+=1    


    print(temp)