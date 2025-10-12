n = int(input())          # number of characters (not actually needed for logic)
s = input()               # input string

# convert to lowercase and make a set of characters
letters = set(s.lower())

# check if all 26 letters are present
if len(letters) >= 26:
    print("YES")
else:
    print("NO")
