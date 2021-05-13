a = []
rows = 0
column = 0
while True:
    b = input()
    if b == "end": break
    a.extend([int(i) for i in b.split()])
    if column == 0: column = len(a)
    rows += 1
print(a, rows, column)
for i in range(rows):
    for j in range(column):
        print(a[i*column+j], end=" ")
    print()
