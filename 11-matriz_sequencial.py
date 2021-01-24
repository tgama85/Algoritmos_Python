#11.Fazer uma busca sequencial em uma matriz 
# (Criar uma matriz 10 linhas e 10 colunas e 
# pedir para o usuário fazer uma busca)

#matriz de 10 linha e 10 colunas
matriz = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]

selecao = int(input(f"Escolha um número de 0 a 99 na matriz {matriz}:")) #busca do usuário

i = 0   #contador linha
j = 0   #contador coluna
paraloop = False    #verifica se o item foi encontrado
for linha in matriz:    #busca nas linhas da matriz
    for coluna in linha:    #busca nas colunas da matriz
        if(coluna == selecao): #comparação da busca do usuário
            print(f"Encontramos o {coluna} na linha {i} e na coluna {j}") #resultado
            paraloop = True
            break
        j += 1  #incrementa coluna
    if paraloop:
        break
    i += 1  #incrementa linha
    j = 0   #sai da coluna
if paraloop == False:
    print("Erro! O número não está na matriz.")