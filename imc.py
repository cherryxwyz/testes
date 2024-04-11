print("cálculo do imc")
peso = float(input("digite um peso: "))
altura = float(input("digite uma altura: "))
imc = (peso / (altura * altura))
if imc < 18.5:
    print("está magro")
elif 18.5 <= imc <= 24.9:
    print("está normal")
else:
    print("está obeso")

