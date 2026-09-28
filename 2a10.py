
idade = int(input("Digite a sua idade:"))

resultado1 = idade >= 18
resultado2 = not resultado1

if resultado1:
    print("Você é adulto.")
if resultado2:
    print("Você é criança")