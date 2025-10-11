a,b=map(int,input().split())
o1=0
o2=0

x=list(map(int,input().split()))
for n in range(a):
    if x[n]<=b:
        o1+=1
    else:
        o2+=2    
print(o1+o2)