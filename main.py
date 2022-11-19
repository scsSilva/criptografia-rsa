while True:
    option = int(input(print("Escolha uma opção abaixo:\n[1] - Gerar chave pública\n[2] - Encriptar mensagem\n[3] - Desencriptar mensagem\n[4] - Sair\n\nOPÇÃO: ")))

    if option == 1:
        print("Gerar chave pública")
    elif option == 2:
        print("Criptografar mensagem")
    elif option == 3:
        print("Desencriptar mensagem")
    elif option == 4:
        break
    else:
        print("Informe uma opção válida")