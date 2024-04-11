print("coloque as medidas desejadas para os três lados do triângulo")
lado1 = int(input("lado 1: "))
lado2 = int(input("lado 2: "))
lado3 = int(input("lado 3: "))
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero")
elif lado1 != lado2 != lado3:
    print("O triângulo é escaleno")
else:
    print("O triângulo é isósceles")
