while True:
    print("\n Escolha um triangulo retangulo : ")
    print("\n\t 1. Normal")
    print("\t 2. Retângulo inverido horizontal")
    print("\t 3. Retângulo inverido verticalmente")
    print("\n Outras Opções: ")
    print("\n\t 4. Losangulo")
    print("\t 5. Quadrado")
    print("\t 0. Sair")

    try : tipo = int(input("\n Escolha: "))
    except: tipo = -1

    if tipo >= 0 and tipo <= 5 : break

print()

#triangulo normal
if tipo == 1 :
    for i in range(10):
        for j in range(i): 
            print('*', end='')
        print()

#triangulo invertido horizontal
if tipo == 2 :
    for i in range(10):
        for j in range(10, i, -1): 
            print('*', end='')
        print()

#triangulo invertido verticalmente

if tipo == 3:
    for i in range(10):
        for k in range(10 - i):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()

#losangulo
if tipo == 4:
    for i in range(1, 10):
        for j in range(10 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")  
        print()

    for i in range(8, 0, -1):
        for j in range(10 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

#quadrado
# if tipo == 5: