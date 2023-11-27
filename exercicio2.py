nome = input("digite seu nome:\n")
idade = float(input(f"digite a idade {nome}:\n"))

if idade < 16:
    print(f" {nome} não pode votar")

elif idade >= 16 and idade < 17:
    print(f" {nome} tem voto facultativo")
elif idade >= 18 and idade < 70:
    print(f" {nome} tem voto obrigatório")


else:
    print(f" {nome} tem voto facultativo")