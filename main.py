import os.path

def mdc(n1, n2):
    if (n1 % n2 == 0):
        return n2
    else:
        return mdc(n2, n1 % n2)

def modularInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

def encrypt(m, e, n):
    result = (m ** e) % n
    return result

def decrypt(c, d, n):
    result = (c ** d) % n
    return result

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

private = None

while True:
    option = int(input("Escolha uma opção abaixo:\n[1] - Gerar chave pública\n[2] - Encriptar mensagem\n[3] - Desencriptar mensagem\n[4] - Sair\n\nOPÇÃO: "))

    if option == 1:
        p = int(input("Informe um número primo P: "))
        q = int(input("Agora, informe outro número primo Q: "))

        n = p * q
        phi = (p - 1) * (q - 1)

        listPrimes = []

        for number in range(2, phi):
            if mdc(phi, number) == 1:
                listPrimes.append(number)
        
        for index in range(len(listPrimes)):
            if index == len(listPrimes) - 1:
                print(f"{listPrimes[index]}")
            else:
                print(f"{listPrimes[index]}", end=" - ")

        e = int(input("Escolha um dos números acima: "))

        if (os.path.exists('key.txt')):
            key = open("key.txt", "w")
            key.write(f"N = {n}\nE = {e}")
            key.close()
        else:
            key = open("key.txt", "a")
            key.write(f"N = {n}\nE = {e}")
            key.close()

        print("Chave pública criada com sucesso. Para consultá-la, verifique o arquivo key.txt")
        print(f"Valor de E: {e}")

    elif option == 2:
        msg = str(input("Digite a mensagem que deseja encriptar: "))
        print("\nAgora informe a chave pública gerada\n")
        n = int(input("Chave N: "))
        e = int(input("Chave E: "))

        message = msg.upper()

        encryptedMessage = []

        for x in range(0, len(message)):
            print(f'{characters.index(message[x]) + 2}')
            code = encrypt(characters.index(message[x]) + 2, e, n)
            encryptedMessage.append(str(code))

        if (os.path.exists('encrypted_message.txt')):
            archiveMessage = open("encrypted_message.txt", "w")
            archiveMessage.write(f"{encryptedMessage}")
            archiveMessage.close()
        else:
            archiveMessage = open("encrypted_message.txt", "a")
            archiveMessage.write(f"{encryptedMessage}")
            archiveMessage.close()

        print("Mensagem criptografada com sucesso. Verifique em encrypted_message.txt")

    elif option == 3:
        print("Informe os valores de P, Q e E\n")
        p = int(input("Valor de P: "))
        q = int(input("Valor de Q: "))
        e = int(input("Valor de E: "))

        phi = (p - 1) * (q - 1)
        private = modularInverse(e, phi)

        message = open("encrypted_message.txt", "r")
        encrypted = eval(message.readlines()[0])
        
        codes = []
        original = ""

        for x in range(0, len(encrypted)):
            code = decrypt(int(encrypted[x]), private, p * q)
            codes.append(code)

        for x in range(0, len(codes)):
            character = characters[codes[x] - 2]
            original += character

        if (os.path.exists('decrypted_message.txt')):
            decryptedMessage = open('decrypted_message.txt', 'w')
            decryptedMessage.write(original)
            decryptedMessage.close()
        else:
            decryptedMessage = open('decrypted_message.txt', 'a')
            decryptedMessage.write(original)
            decryptedMessage.close()

        print("Mensagem descriptografada com sucesso. Verifique a mensagem no arquivo decrypted_message.txt")
    elif option == 4:
        break
    else:
        print("Informe uma opção válida")