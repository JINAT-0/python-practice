n=int(input())
for _ in range(n):
    x=int(input())
    if x>=1900:
        print("Division 1")
    elif 1600<=x<=1899:
        print("Division 2")
    elif 1400<=x<=1599:
        print("Division 3")
    elif x<=1399:
        print("Division 4")