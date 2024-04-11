operacao = input("digite a operação desejada (soma, subtracao, multiplicacao ou divisao): ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
def calcular (n1, n2):
  match operacao:
    case "soma":
      return n1 + n2
    case "subtracao":
      return n1 - n2
    case "multiplicacao":
      return n1 * n2
    case "divisao":
      if n2 == 0:
        raise ValueError("divisão por zero.")
      return n1 / n2
    case _:
      raise ValueError("Operação inválida.")

