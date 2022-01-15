n = 6
m =n
for i in range(n):
    for k in range(m):
        print(" ",end =" ")
    for j in range(i):
        print(" * ",end = " ")
    print()
    m = m - 1

m = 0
for i in range(n, 0, -1):
    for k in range(m):
        print(" ", end = " ")
    for j in range(i):
        print(" * ", end = " ")
    print()
    m = m + 1
