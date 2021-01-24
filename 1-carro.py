#1.Algoritmo para ligar um carro (Imprimir a sequência para ligar um carro)
#Passo a passo: Coloca a chave no miolo de ignição, Segurar embragem, verificar cambio ponto morto e girar a chave

print("Bem-vinde ao ligue o seu carro!")
#Passo1
usuario_carro = str(input('Você está fora do carro?(S/N)'))
var1 = "S"
var2 = "N"
if usuario_carro == var1:   #verifica resposta Sim do usuário do carro
    print("Abra a porta do carro, entre e sente no banco do motorista.")
elif usuario_carro == var2: #verifica resposta Não do usuário do carro
    print("Vamos continuar então!")
else:   #verifica se usuário não digitou Sim(S) ou Não(N)
    print("Você precisa digitar S para sim ou N para Não.")
#Passo2
usuario_carro= str(input('Você está sentado no banco do motorista?(S/N)'))
if usuario_carro == var1:
    print("Coloque a chave no miolo da ignição.")
elif usuario_carro == var2:
    print("Você precisa estar no banco do motorista para dirigir!")
else:
    print("Sério! Você precisa digitar S para sim ou N para Não.")
#Passo3
usuario_carro= str(input('Você colocou a chave na ignição?(S/N)'))
if usuario_carro == var1:
    print("Segure a embragem.")
elif usuario_carro == var2:
    print("Você precisa colocar a chave na ignição para dirigir!")
else:
    print("Mais uma vez, lembre, S para sim e N para não.")
#Passo4
usuario_carro= str(input('Você segurou a embreagem?(S/N)'))
if usuario_carro == var1:
    print("Verifique se o cambio está em ponto morto.")
elif usuario_carro == var2:
    print("Você precisa segurar a embragem para dirigir!")
else:
    print("Reforçando, S para sim e N para não.")
#Passo5
usuario_carro= str(input('O cambio está no ponto morto?(S/N)'))
if usuario_carro == var1:
    print("Gire a chave.")
elif usuario_carro == var2:
    print("O cambio precisa estar no ponto morto para dirigir!")
else:
    print("Começamos a pensar que não deseja ligar o carro.")
#Passo6
usuario_carro= str(input('Você girou a chave?(S/N)'))
if usuario_carro == var1:
    print("Parabéns! Você ligou o carro!")
elif usuario_carro == var2:
    print("Você precisa girar a chave para dirigir!")
    print("Você não quer dirigir o carro!")
else:
    print("Última chance, S para sim e N para não.")
    usuario_carro = str(input('Você girou a chave?(S/N)'))
    if usuario_carro == var1:
        print("Parabéns! Você ligou o carro!")
    elif usuario_carro == var2:
        print("Você não quer dirigir o carro!")
    else:
        print("É definitivo! Você não quer ligar o carro.")