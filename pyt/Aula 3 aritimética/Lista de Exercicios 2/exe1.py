#Peça ao usuário para digitar sua idade atual e, em seguida, pergunte em quantos anos ele deseja saber sua idade no futuro. Exiba o resultado.

idade = int(input("Digite sua idade: "))
anosfuturos = int(input("Você quer saber sua idade daqui a quantos anos: "))

idadefutura = idade + anosfuturos
mensagem = f"Sua idade atual é {idade}, e daqui a {anosfuturos} você tera {idadefutura} anos"
print(mensagem)
