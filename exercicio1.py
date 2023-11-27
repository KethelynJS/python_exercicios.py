nome = input("digite o nome do contribuinte:\n")
salariomensal = float(input(f"digite o salario mensal do {nome}:\n"))

if salariomensal < 1903.98:
    print(f"O contribuinte {nome} está insento")

elif salariomensal >= 1903.99 and salariomensal < 2826.65:
    print(f"O contribuinte {nome} pagará 7,5% de imposto")
elif salariomensal >= 2826.66 and salariomensal < 3751.05:
    print(f"O contribuinte {nome} pagará 15% de imposto")
elif salariomensal >= 3751.06 and salariomensal < 4664.68:
    print(f"O contribuinte {nome} pagará 22.5%% de imposto")


else:
    print(f"O contribuinte {nome} pagará 27.5% de imposto")