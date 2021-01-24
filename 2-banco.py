#2.Algoritmo para ir ao banco para sacar dinheiro (Imprimir a sequência para ir ao banco e sacar dinheiro)
#Passo ao passo: endereço do banco, transporte para chegar ao banco, localizar caixa eletrônico e cartão
#de acesso a conta, digital de confirmação e senha do banco, digite o valor desejado, saque o dinheiro

print("Bem-vinde ao saque o dinheiro no banco!")
#Passo1
usuario_banco = str(input('Você sabe o endereço do banco?(S/N)'))
var1 = "S"
var2 = "N"
if usuario_banco == var1:
    print("Vamos continuar então!")
elif usuario_banco == var2:
    print("Recomendamos que localize o banco mais próximo de você.")
else:
    print("Você precisa usar S para sim e N para não.")
#Passo2
usuario_banco = str(input('Você precisa de transporte para chegar ao banco?(S/N)'))
if usuario_banco == var1:
    print("Recomendamos que localize o melhor transporte para você chegar ao banco.")
elif usuario_banco == var2:
    print("Podemos continuar então!")
else:
    print("Sério! Você precisa usar S para sim e N para não.")
#Passo3
usuario_banco = str(input('Chegando ao banco, encontre o caixa eletrônico, achou?(S/N)'))
if usuario_banco == var1:
    print("Dirija-se ao caixa eletrônico e insira o cartão bancário.")
elif usuario_banco == var2:
    print("Localize um balcão de informações que o ajude a localizar um caixa para saque.")
else:
    print("Mais uma vez, lembre, S para sim e N para não.")
#Passo4
usuario_banco = str(input('Você trouxe o cartão bancário?(S/N)'))
if usuario_banco == var1:
    print("Após inserir o cartão, confirme sua senha por reconhecimento de impressão digital ou digite a senha.")
elif usuario_banco == var2:
    print("Você precisa do seu cartão para prosseguir com o saque.")
else:
    print("Reforçando, S para sim e N para não.")
#Passo5
usuario_banco = str(input('Confirmou seus dados bancários no caixa eletrônico?(S/N)'))
if usuario_banco == var1:
    print("Na tela clique na opção Saque e escolha a quantia desejada.")
elif usuario_banco == var2:
    print("Sem a confirmação dos seus dados não é possível usar o Saque do Banco.")
else:
    print("Começamos a pensar que você não quer realizar o Saque.")
#Passo6
usuario_banco = str(input('Após confirmar a quantia, o dinheiro foi entregue pela máquina?(S/N)'))
if usuario_banco == var1:
    print("Parabéns! Você sacaou o dinheiro no Banco!")
elif usuario_banco == var2:
    print("É provavél que você não tenha a quantia desejada, dirija-se a um caixa de atendimento para orientações.")
else:
    print("É definitivo! Você não quer usar o Saque do Banco.")
