# Lab 09 - Festival Decoration Designer

rows = int(input("Enter the number of rows: "))

print("Pattern 1: Star Triangle")
print("-" * 30)
for i in range(1, rows + 1):
    print("* " * i)

print("\nPattern 2: Number Triangle")
print("-" * 30)
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 3: Inverted Star Triangle")
print("-" * 30)
for i in range(rows, 0, -1):
    print("* " * i)

print("\nPattern 4: Pyramid")
print("-" * 30)
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)
