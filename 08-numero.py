#8.Elabore um algoritmo em Python que receba um número 
#inteiro e escreva na tela o número fornecido, o antecessor 
#desse número e o sucessor desse número; 

numero = int(input("Digite um número: "))   #solicita número ao usuário
print(f"Seu número foi {numero}")   #numero digitado pelo usuário
numero -= 1 #operação antesessor n - 1
print(f"O antessor é {numero}")
numero += 2 #operação sucessor (n - 1) + 1
print(f"O sucessor é {numero}")