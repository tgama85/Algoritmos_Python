#7.Fazer um sistema de Loteria (Deve pedir o nome do usuário, 
#pedir um número e comparar com um conjunto aleatório de número 
#(de 0 a 100) e dizer se o usuário adivinhou) 

from random import randint #parâmentro para buscar número inteiro

usuario = input("Digite o seu nome: ")  #solicita nome do usuário
num = input("Digite um número de 0 a 100: ")    #solicita um número ao usuário

lista = randint(0,100) #comando faz o sorteio da loteria
if num == lista:    #verifica se num é igual a lista
    #imprime o resultado da loteria
    print(f"{usuario} adivinhou o número da loteria! " + "O número da Loteria foi {}.".format(lista))
else:
    print(f"{usuario} não foi dessa vez! " + "O número da Loteria foi {}.".format(lista))

