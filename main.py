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

def createFile(name, content):
    file = open(f'{name}.txt', 'a')
    file.write(f'{content}')
    file.close()

def updateContentFile(name, content):
    file = open(f'{name}.txt', 'w')
    file.write(f'{content}')
    file.close()

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

while True:
    option = int(input('Escolha uma opção abaixo:\n[1] - Gerar chave pública\n[2] - Encriptar mensagem\n[3] - Desencriptar mensagem\n[4] - Sair\n\nOPÇÃO: '))

    if option == 1:
        p = int(input('Informe um número primo P: '))
        q = int(input('Agora, informe outro número primo Q: '))

        n = p * q
        phi = (p - 1) * (q - 1)

        listPrimes = []

        for number in range(2, phi):
            if mdc(phi, number) == 1:
                listPrimes.append(number)
        
        for index in range(len(listPrimes)):
            if index == len(listPrimes) - 1:
                print(f'{listPrimes[index]}')
            else:
                print(f'{listPrimes[index]}', end=' - ')

        e = int(input('Escolha um dos números acima: '))

        if (os.path.exists('key.txt')):
            updateContentFile('key', f'N = {n}\nE = {e}')
        else:
            createFile('key', f'N = {n}\nE = {e}')

        print('Chave pública criada com sucesso. Para consultá-la, verifique o arquivo key.txt')

    elif option == 2:
        msg = str(input('Digite a mensagem que deseja encriptar: '))
        print('\nAgora informe a chave pública gerada\n')
        n = int(input('Chave N: '))
        e = int(input('Chave E: '))

        message = msg.upper()

        encryptedMessage = ''

        for x in range(0, len(message)):
            code = encrypt(characters.index(message[x]) + 2, e, n)
            encryptedMessage += f'{str(code)} '

        if (os.path.exists('encrypted_message.txt')):
            updateContentFile('encrypted_message', encryptedMessage)
        else:
            createFile('encrypted_message', encryptedMessage)

        print('Mensagem criptografada com sucesso. Verifique em encrypted_message.txt')

    elif option == 3:
        print('Informe os valores de P, Q e E\n')
        p = int(input('Valor de P: '))
        q = int(input('Valor de Q: '))
        e = int(input('Valor de E: '))

        phi = (p - 1) * (q - 1)
        private = modularInverse(e, phi)

        message = open('encrypted_message.txt', 'r')
        encrypted = message.readlines()[0].split()
        
        codes = []
        original = ''

        for x in range(0, len(encrypted)):
            code = decrypt(int(encrypted[x]), private, p * q)
            codes.append(code)

        for x in range(0, len(codes)):
            character = characters[codes[x] - 2]
            original += character

        if (os.path.exists('decrypted_message.txt')):
            updateContentFile('decrypted_message', original)
        else:
            createFile('decrypted_message', original)

        print('Mensagem descriptografada com sucesso. Verifique a mensagem no arquivo decrypted_message.txt')
    elif option == 4:
        break
    else:
        print('Informe uma opção válida')
