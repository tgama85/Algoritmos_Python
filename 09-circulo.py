#9.Elabore um algoritmo em Python que calcule a 
# área e o perímetro de um círculo, sabendo que 
# A = πr² e P=2πr. 

raio = float(input("Digite o tamanho do raio do círculo: "))    #solicita o raio
area = float((raio**2)*3.14)    #cálculo da área do círculo
perimetro = float(2*3.14*raio)  #cálculo do perímeto do cículo
print("A área do círculo é %.2f"%area + " e seu prímetro é %.2f"%perimetro) #resultado