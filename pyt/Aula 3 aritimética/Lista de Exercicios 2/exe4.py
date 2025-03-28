#Peça ao usuário um número de minutos e converta para horas e minutos.

minutos = int(input("Digite um numero de minutos: "))
horas = minutos // 60
minutohoras = minutos % 60
mensagem = f"{minutos} é equivalente a {horas} horas e {minutohoras} minutos"
print(mensagem)