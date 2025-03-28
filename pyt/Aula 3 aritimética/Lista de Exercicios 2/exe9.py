#Peça a velocidade média e o tempo de viagem e calcule a distância percorrida.

velocidade = int(input("Informe a velocidade média (km/h): "))
tempoviagem = float(input("Informe o tempo de viagem (horas): "))

calculo = velocidade * tempoviagem
mensagem = f"A distancia percorrida foi: {calculo} km"
print(mensagem)