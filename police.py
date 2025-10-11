n=int(input())

a=list(map(int,input().split()))
av=0
un=0
for e in a:
    if e==-1:
       if av>0:
          av-=1
       else:
          un+=1
    else :
        av+=e    
print(un)