pesoDinheiro = input().split(" ")

peso = int(pesoDinheiro[0])
dinheiro = int(pesoDinheiro[1])

if 1 <= peso <= 2500 and 1 <= dinheiro <= 500:
    for i in range(0, dinheiro):
        valor = int(input())

        if valor == 500 or valor == 200 or valor == 100 or valor == 50 or valor == 20 or valor == 10 or valor == 5:
            # notas
        elif valor == 2 or valor == 1:
            # moedas
        else: