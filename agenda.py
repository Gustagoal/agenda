from datetime import datetime

data_atual = datetime.now().strftime("%d_%m_%Y")

nome = f"{data_atual}.txt"


with open(nome, "w") as arquivo:
    lista = input("Digite o seu dia: ")
    arquivo.write(lista)
    print("Dia salvo com sucesso")
