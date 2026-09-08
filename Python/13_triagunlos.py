for i in range(10):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(10):
    for j in range(10, i,-1):
        print("*", end=" ")
    print()

for i in range(10):
    for j in range(10 - i, 0, -1):
        print(" ", end=" ")
    for k in range(0, i):
            print("*", end=" ")
    print()

for i in range(10):
    for j in range(10 - i, 0, -1): print(' ', end='')
    for k in range(0, i): print("*", end='')
    for j in range(i-1): print("*", end='')

    print()

for i in range(10):
    for k in range(i): print(" ", end="")
    for j in range(10 - i, 0, -1) : print("*",end="")
    for j in range(10 - 1, i, -1): print("*", end="")

    print()
