# i = 0
# while i < 2:
#     print(i)
#     i += 1

# for => quantidade de ciclos (repetições) que vou fazer. 
# while => quando não sei quantas vezes vou fazer. 

preco = 30 
dinheiro = 0

while True:

    while True:
        moeda = int(input("Introduza uma moeda: "))
        if moeda >= 0: break

    dinheiro += moeda 

    troco = dinheiro - preco

    print(preco, dinheiro, troco)

    if troco >= 0 : break
