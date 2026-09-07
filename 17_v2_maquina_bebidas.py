
# import os
# os.system('cls')

import subprocess

while True:

    # subprocess.run('cls',shell=True)

    # 1. Menu de bebidas

    while True :
        print('\n MENU')
        print('\t 1. Café')
        print('\t 2. Chá')
        print('\t 3. Chocolate')

        try   : opcao = int(input('\n Escolha a sua bebida: '))
        except: opcao = -1

        if (opcao > 0 and opcao <= 3) or opcao == 123 : break

    print()

    # proviório ... sair do programa
    if opcao == 123 : break

    # 2. Escolher o preço do produto

    match opcao:
        case 1: preco = 35
        case 2: preco = 45
        case 3: preco = 50

    print(' PREÇO do produto:', preco,'cêntimos \n')

    # 3. Receber moedas válidas

    dinheiro = 0

    while True:
        try: moeda = int( input(' Introduza uma moeda válida: ') )
        except: moeda = 0

        if moeda == 5 or moeda == 10 or moeda == 20 or moeda == 50 or moeda == 100 or moeda == 200: 
            dinheiro = dinheiro + moeda
            troco = preco - dinheiro 

            if troco <= 0 : break
            print(' TROCO:', troco, 'cêntimos \n')


    # 4. Devolução do troco em moedas

    troco *= -1
    print(' TROCO:', troco, 'cêntimos \n')

    moedaatual = 200
    m5 = m10 = m20 = m50 = m100 = m200 = 0  

    if troco > 0:
        while True:

            print(troco, moedaatual)

            temp = troco - moedaatual
            # trocar moedas
            if temp < 0 :
                if moedaatual == 200 : moedaatual = 100
                else : 
                    if moedaatual == 100 : moedaatual = 50; 
                    else :
                        if moedaatual == 50 : moedaatual = 20
                        else :
                            if moedaatual == 20 : moedaatual = 10
                            else : moedaatual = 5
            else : troco = troco - moedaatual

            if troco == 0 : break
    
        print()

    


