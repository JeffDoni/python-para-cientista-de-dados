import pandas as pd
import numpy as np


# 1. Some o valor 10 com 30 e exiba na tela

print(10 + 30)

# 2. Some os seguintes números: 10, 300, 0.4, 10

print(10 + 300 + 0.4 + 10)
np.sum([10, 300, 0.4, 10])

# 3. Desenvolva comandos em Python capaz de calcular a média harmônica entre 5 números. Por exemplo: 2, 3, 5, 6 e 9

print((5 / (1/2 + 1/3 + 1/5 + 1/6 + 1/9)))


# 4. Um Cientista de Dados Jr precisa criar sequência de comandos que seja
# capaz de calcular a média ponderada dos valores digitados pelo usuário.
# O usuário é capaz de digitar 8 valores. O primeiro número tem peso 0.5 ,
# o segundo 1.0, o terceiro 1.5 até o último valor que tem peso 4, ou seja,
# os pesos são acrescidos de 0.5 para cada valor. Portanto, o algoritmo
# deve ser capaz de calcular a média ponderada dos oito valores digitados
# pelo usuário, cada valor com o seu respectivo peso.

# valor_01 = input( "Digite o primeiro valor" )
# valor_02 = input( "Digite o segundo valor" )
# valor_03 = input( "Digite o terceiro valor" )
# valor_04 = input( "Digite o quarto valor" )


x1 = 0.5
x2 = 1.0
x3 = 1.5
x4 = 2.0
x5 = 2.5
x6 = 3.0
x7 = 3.5
x8 = 4.0

valor_01 = float(input("Digite o primeiro valor: "))
valor_02 = float(input("Digite o segundo valor: "))
valor_03 = float(input("Digite o terceiro valor: "))
valor_04 = float(input("Digite o quarto valor: "))
valor_05 = float(input("Digite o quinto valor: "))
valor_06 = float(input("Digite o sexto valor: "))
valor_07 = float(input("Digite o sétimo valor: "))
valor_08 = float(input("Digite o oitavo valor: "))

numerador = (valor_01 * x1) + (valor_02 * x2) + (valor_03 * x3) + (valor_04 * x4) + (valor_05 * x5) + (valor_06 * x6) + (valor_07 * x7) + (valor_08 * x8)
denominador = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

media_ponderada = numerador / denominador
print(media_ponderada)

# 5. Um programador Jr precisa construir uma mini calculadora. Essa
# calculadora segue os seguintes padrões:
# a. Se o usuário digital um valor menor ou igual a 5, a calculadora vai
# multiplicar esse valor por 10 e retornar o valor resultantes para o
# usuário

valor = float(input("Digite um valor: "))
if valor <= 5:
    print(valor * 10)

# b. Se o usuário digitar um número entre 6 e 10, a calculadora multiplica
# por 20 o número digitado pelo usuário

elif valor >= 6 and valor <= 10:
    print(valor * 20)

# c. Se o usuário digitar um valor maior ou igual a 11, a calculadora soma
# 100 ao número digitado. Ajude o programador Jr a construir essa
# calculadora, fornecendo os comandos em Python para ele.

elif valor >= 11:
    print(valor + 100)




# 6. Um programador Jr precisa criar um algoritmo que consiga fazer a
# comparação entre três valores e exibir qual é o maior e qual é o menor
# valor digitado. Ajude o programador desenvolvendo o código em Python.

valor_01 = float(input("Digite o primeiro valor: "))
valor_02 = float(input("Digite o segundo valor: "))
valor_03 = float(input("Digite o terceiro valor: "))
if valor_01 > valor_02 and valor_01 > valor_03:
    print("O maior valor é: ", valor_01)
elif valor_02 > valor_01 and valor_02 > valor_03:
    print("O maior valor é: ", valor_02)
elif valor_03 > valor_01 and valor_03 > valor_02:
    print("O maior valor é: ", valor_03)
if valor_01 < valor_02 and valor_01 < valor_03:
    print("O menor valor é: ", valor_01)
elif valor_02 < valor_01 and valor_02 < valor_03:
    print("O menor valor é: ", valor_02)
elif valor_03 < valor_01 and valor_03 < valor_02:
    print("O menor valor é: ", valor_03)
    