n=int(input())
for _ in range(n):
    m=list(map(int,input()))
    x=m[0]+m[1]+m[2]
    y=m[3]+m[4]+m[5]
    if x==y:
      print("YES")
    else:
      print("NO")         