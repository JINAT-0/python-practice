total = int(input("Enter Total Memory: "))
os = int(input("Enter OS Memory: "))

available = total - os

n = int(input("Enter Number of Processes: "))
p = list(map(int, input("Enter Process Sizes: ").split()))

used = 0
count = 0

for i in range(n):
    if used + p[i] <= available:
        print("Process", i+1, "Allocated")
        used += p[i]
        count += 1
    else:
        print("Process", i+1, "Not Allocated")

free = available - used

print("Total Processes:", n)
print("Allocated Processes:", count)
print("Used Memory:", used)
print("Free Memory:", free)