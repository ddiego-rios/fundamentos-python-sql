
print('\n Escolha um triângulo retângulo: ')

print('\n\t 1. normal')
print('\t 2. invertido horizontal')
print('\t 3. invertido verticalmente')

tipo = int( input('\n Escolha: ') )

print()

if tipo == 1 :
    for i in range(10):
        for j in range(i): 
            print('*', end='')
        print()

if tipo == 2 :
    for i in range(10):
        for j in range(10, i, -1): 
            print('*', end='')
        print()

