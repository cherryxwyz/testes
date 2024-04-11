bim1 = float(input("digite a nota do primeiro: "))
bim2 = float(input("digite a nota do segundo: "))
tab1 = float(input("digite a nota do trabalho do segundo bimestre: "))
if (bim1 + bim2 + tab1) / 3 < 7:
    print("vai ter que estudar em")
else:
    print("tenta continuar na média, colega")
bim3 = float(input("digite a nota do terceiro: "))
bim4 = float(input("digite a nota do quarto bimestre: "))
media = (bim1 + bim2 + tab1 + bim3 + bim4) / 5
if media >= 7:
    print("passou de ano, relaxa")
else:
    print("reprovado, eu avisei que era pra estudar, ai ai")
