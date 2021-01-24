#4.Elabore um algoritmo em Python que leia, calcule e escreva a 
#média aritmética entre quatro números

#solicita os 4 números
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
num4 = float(input("Digite a quarta nota: "))

media = (num1 + num2 + num3 + num4)/4   #executa operação matemática
print("%0.1f é a média aritmética."%media)  #imprime resultado