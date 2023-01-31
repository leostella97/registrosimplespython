nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")
email = input("Digite seu endereço de e-mail: ")

print("Os dados estão corretos?", nome, idade, email, sep="\n")
resposta = input("Escreva sua resposta com S para SIM e N para NÃO: \n")

if (resposta == "S" or resposta == "s"):
    print("Informações cadastradas com sucesso!")
elif (resposta == "N" or resposta =="n"):
    print("As informações não foram incluídas no banco de dados, favor reiniciar o aplicativo.")
else:
    print("Por favor, responder com S ou N, reinicie o aplicativo.")