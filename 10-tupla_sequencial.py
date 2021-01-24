#10.Fazer uma busca sequencial em uma lista 
# (Criar uma tupla [0....20] e pedir para o 
# usuário fazer uma busca)
# orientação do professor = use um while e cada iteração será como se fosse navegar no índice

num_usuario = int(input("Procure por um número de 0 a 20: "))   #busca do usuário
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
busca = 0   #contador da busca
paraloop = False    #verifica se o item foi encontrado
while busca <= 20:
    if num_usuario in tupla:    #condição para buscar o número do usuário na tupla
        #fazendo a busca com o index
        print(f"O indíce do número {num_usuario} é {tupla.index(num_usuario)}")    
        paraloop = True
        break
    busca += 1   #incrementa busca
if paraloop == False:
    print("Erro! O número não está na tupla.")

    
#2ª solução com função (alternativa)

# num_usuario = int(input("Procure por um número de 0 a 20: "))
# tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

# def busca(tupla, num_usuario):    #função de busca
#   if num_usuario in tupla:
#     return tupla.index(num_usuario)   #indice que percorre a tupla em busca do número
#   else:
#     return "Erro! O número não está na tupla."   #erro se o usuário digitar número/caracter fora da tupla

# print(busca(tupla, num_usuario))  #resultado

