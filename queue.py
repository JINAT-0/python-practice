n = int(input("Enter number of processes: "))
q = int(input("Enter number of queues: "))

queues = []

for i in range(q):
    queues.append([])

for i in range(n):
    name = input("Enter process name: ")
    queue = int(input("Enter queue number: "))
    burst = int(input("Enter burst time: "))

    queues[queue - 1].append((name, burst))

print("\nExecution Order:")


for i in range(q):
    print("Queue", i + 1)

    for p in queues[i]:
        print(p[0], "=", p[1], "ms")