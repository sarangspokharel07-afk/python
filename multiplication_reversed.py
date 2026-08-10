#print the multiplication table of n in reversed order.
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} * {i} = {n * i}")
