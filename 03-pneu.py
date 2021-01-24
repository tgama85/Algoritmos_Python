#3.Algoritmo para trocar o pneu do carro (Imprimir a sequência para trocar o pneu do carro) 
#Passo a passo: Encontre um lugar plano, estável e seguro para estacionar e trocar o pneu; 
                #Puxe o freio de mão e ponha o câmbio em modo "estacionado". 
                #Ponha um objeto pesado (por exemplo, uma pedra, um pedaço de concreto, 
                #uma roda sobressalente, entre outros) em frente às rodas dianteiras e traseiras do carro.
                #Pegue o estepe e o macaco, levante o macaco até que ele apoie o carro (sem levantá-lo do chão).
                #Tire a calota e afrouxe os parafusos (girando a chave de roda em sentido anti-horário).
                #Acione o macaco para levantar o pneu um pouco mais e remova os parafusos totalmente.
                #Retire o pneu furado e coloque-o sob o veículo — caso o macaco venha a ceder, ele amortecerá a queda, 
                #diminuindo o risco de acidentes.
                #Ponha o estepe no eixo e aperte os parafusos à mão até onde puder. 
                #Ao abaixar o carro, não permita que o peso fique apoiado no novo pneu, termine de descer o carro e retire o macaco.
                #Coloque o antigo pneu no porta-malas e leve-o ao borracheiro.

print("Bem-vinde ao troque o pneu do seu carro!")
print("Passo 1: Encontre um lugar plano, estável e seguro para estacionar e trocar o pneu.")
#Passo1
usuario_pneu = str(input("Cumpriu o Passo 1?(S/N)"))
var1 = "S"
var2 = "N"
#Passo2
if usuario_pneu == var1:
    print("Passo 2: Puxe o freio de mão e ponha o câmbio em modo 'estacionado'")
elif usuario_pneu == var2:
    print("Realize o Passo 1 por segurança.")
    print("Se está seguro, Passo 2: Puxe o freio de mão e ponha o câmbio em modo 'estacionado'")
else: 
    print("Você precisa usar S para sim e N para não.")
#Passo3
usuario_pneu = str(input("Cumpriu o Passo 2?(S/N)"))
if usuario_pneu == var1:
    print("Passo 3: Ponha um objeto pesado (por exemplo, uma pedra, um pedaço de concreto,\n uma roda sobressalente, entre outros) em frente às rodas dianteiras e traseiras do carro.")
elif usuario_pneu == var2:
    print("Realize o Passo 2 por segurança.")
    print("Se está seguro, Passo 3: Ponha um objeto pesado (por exemplo, uma pedra, um pedaço de concreto,\n uma roda sobressalente, entre outros) em frente às rodas dianteiras e traseiras do carro.")
else:
    print("Mais uma vez, lembre, S para sim e N para não.")
#Passo4
usuario_pneu = str(input("Cumpriu o Passo 3?(S/N)"))
if usuario_pneu == var1:
    print("Passo 4: Pegue o estepe e o macaco, levante o macaco até que ele apoie o carro (sem levantá-lo do chão).")
elif usuario_pneu:
    print("Realize o Passo 3 por segurança.")
    print("Se está seguro, Passo 4: Pegue o estepe e o macaco, levante o macaco até que ele apoie o \n carro (sem levantá-lo do chão).")
else:
    print("Sério! Você precisa digitar S para sim ou N para Não.")
#Passo5
usuario_pneu = str(input("Cumpriu o Passo 4?(S/N)"))
if usuario_pneu == var1:
    print("Passo 5: Tire a calota e afrouxe os parafusos (girando a chave de roda em sentido anti-horário).")
elif usuario_pneu == var2:
    print("Sem o estepe e o pneu, não conseguirá trocar o pneu.")
    print("Se pegou o estepe e o pneu, Passo 5: Tire a calota e afrouxe os parafusos (girando a chave \n de roda em sentido anti-horário).")
else:
    print("Reforçando, S para sim e N para não.")
#Passo6
usuario_pneu = str(input("Cumpriu o Passo 5?(S/N)"))
if usuario_pneu == var1:
    print("Passo 6: Acione o macaco para levantar o pneu um pouco mais e remova os parafusos totalmente.")
elif usuario_pneu == var2:
    print("Se não cumprir o Passo 5, não conseguirá trocar o pneu.")
    print("Se realizou o Passo 5, Passo 6: Acione o macaco para levantar o pneu um pouco mais e remova os \n parafusos totalmente.")
else:
    print("Começamos a pensar que não deseja trocar o pneu.")
#Passo7
usuario_pneu = str(input("Cumpriu o Passo 6?(S/N)"))
if usuario_pneu == var1:
    print("Passo 7: Retire o pneu furado e coloque-o sob o veículo — caso o macaco venha a ceder, ele /n amortecerá a queda, diminuindo o risco de acidentes.")
elif usuario_pneu == var2:
    print("Se não cumprir o Passo 6, não conseguirá trocar o pneu.")
    print("Se removeu os parafusos, Passo 7: Retire o pneu furado e coloque-o sob o veículo — caso o macaco venha a ceder, ele /n amortecerá a queda, diminuindo o risco de acidentes.")
else:
    print("Não entendemos o que digitou, lembre-se S para sim e N para não.")
#Passo8
usuario_pneu = str(input("Cumpriu o Passo 7?(S/N)"))
if usuario_pneu == var1:
    print("Passo 8: Ponha o estepe no eixo e aperte os parafusos à mão até onde puder.")
elif usuario_pneu == var2:
    print("Realize o Passo 7 por segurança.")
    print("Se realizou o Passo 7, Passo 8: Ponha o estepe no eixo e aperte os parafusos à mão até onde puder.")
else:
    print("Não entendemos o que digitou, lembre-se S para sim e N para não.")
#Passo9
usuario_pneu = str(input("Cumpriu o Passo 8?(S/N)"))
if usuario_pneu == var1:
    print("Passo 9: Ao abaixar o carro, não permita que o peso fique apoiado no novo pneu, termine de \n descer o carro e retire o macaco.")
elif usuario_pneu == var2:
    print("Se não apertar os parufusos, o carro não sairá do lugar.")
    print("Se apertou os parafusos, Passo 9: Ao abaixar o carro, não permita que o peso fique apoiado no novo pneu, termine de \n descer o carro e retire o macaco.")
else:
    print("Última chance, S para sim e N para não.")
#Passo10
usuario_pneu = str(input("Cumpriu o Passo 9?(S/N)"))
if usuario_pneu == var1:
    print("Passo 10: Coloque o antigo pneu no porta-malas e leve-o ao borracheiro. Parabéns! Você trocou o pneu!")
elif usuario_pneu == var2:
    print("Se não descer o carro, ele não irá a lugar algum.")
    print("Se desceu o carro, Passo 10: Coloque o antigo pneu no porta-malas e leve-o ao borracheiro. Parabéns! Você trocou o pneu!")
else:
    print("É definitivo! Você não quer trocar o pneu!")
