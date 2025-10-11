t=int(input())
for _ in range(t):
    c=int(input())
    if c%3==0:
        print("0")
    else:
        print (3-(c%3))   