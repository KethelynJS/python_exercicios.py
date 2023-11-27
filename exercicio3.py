nome = input("digite seu nome:\n")
salario = float(input(f"digite o salário de {nome}:\n"))
tempo = float(input(f"digite o tempo de serviço de {nome}:\n"))


if tempo < 1:
    bonificacao = 0
    print(f" {nome} não tem bonificação")
elif 1 <= tempo < 3:
    bonificacao = 0.10 * salario
    print(f"{nome} tem 10% de bonificação: R${bonificacao:.2f}")
elif 3 <= tempo < 6:
    bonificacao = 0.15 * salario
    print(f"{nome} tem 15% de bonificação: R${bonificacao:.2f}")
elif 6 <= tempo < 10:
    bonificacao = 0.20 * salario
    print(f"{nome} tem 20% de bonificação: R${bonificacao:.2f}")
else:
    bonificacao = 0.25 * salario
    print(f"{nome} tem 25% de bonificação: R${bonificacao:.2f}")
