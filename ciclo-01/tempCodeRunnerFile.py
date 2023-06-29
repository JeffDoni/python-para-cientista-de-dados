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
