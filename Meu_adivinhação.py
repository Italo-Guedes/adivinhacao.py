import random
print("****************************************")
print("******Bem vindo ao Jogo*****************")
print("****************************************")

numero_secreto = 10 #random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000


print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível:"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_tentativa = int(input("Digite um número entre 1 e 100:"))

    acertou = chute_tentativa == numero_secreto
    maior   = chute_tentativa > numero_secreto
    menor   = chute_tentativa< numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    if(maior):
        print("Você errou! Seu número foi maior que o número secreto!")
    elif(menor):
        print("Você errou! Seu número foi menor que o número secreto!")
    pontos_perdidos = abs(numero_secreto - chute_tentativa)
    pontos = pontos - pontos_perdidos



print("Fim de jogo!!")
