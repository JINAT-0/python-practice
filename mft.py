total = int(input("Enter Total Memory: "))
os = int(input("Enter OS Memory: "))
part = int(input("Enter Partition Size: "))

n = int(input("Enter Number of Processes: "))
p = list(map(int, input("Enter Process Sizes: ").split()))

available = total - os
tp = available // part
used = 0
frag = 0
count = 0

for i in range(n):
    if p[i] <= part and count < tp:
        print("Process", i+1, "Allocated")
        frag += part - p[i]
        count += 1
    else:
        print("Process", i+1, "Not Allocated")

free = available - used

print("Total Partition:", tp)
print("Used Memory:", used)
print("Free Memory:", free)
print("Internal Fragmentation:", frag)