import string
import random

print('\n Gerador de senhas \n')
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

while True:
    try:
        escolha_usuario = int(input('Digite o tamanho da senha: '))
        quantidade_caracteres = int(escolha_usuario)
        print('Escolha uma opcao: ')
        print('1-Senha basica')
        print('2-Senha forte')
        print('3-Mais informacoes')
        escolha_usuario2 = int(input(''))
        if escolha_usuario2 == 3:
            print('Senha basica: Apenas letras maiusculas e minusculas')
            print('Senha Forte: Letras maiusculas e minusculas, nuemros e simbolos')
            escolha_usuario2 = int(input('Agora escolha uma opcao: '))
        elif escolha_usuario2 > 3 or escolha_usuario2 < 1:
            print('Opcao invalida')
            escolha_usuario2 = int(input('Escolha uma opcao valida: '))
        

        if quantidade_caracteres < 5:
            print('A senha deve ter no minimo 5 caracter')
            escolha_usuario = int(input('Digite o tamanho da senha: '))
        elif quantidade_caracteres > 52:
            print('A senha nao pode ter mais de 52 caracteres')
            escolha_usuario = int(input('Digite o tamanho da senha: '))
        else:
            break
    except ValueError:
        print('Digite apenas numeros')

def senha_basica():
    random.shuffle(s1)
    random.shuffle(s2)
    part1 = round(quantidade_caracteres * (40/100))
    part2 = round(quantidade_caracteres * (40/100))
    part3 = round(quantidade_caracteres * (20/100))

    resultado = []
    for x in range(part1):
        resultado.append(s1[x])
    
    for x in range(part2):
        resultado.append(s2[x])

    for x in range(part3):
        resultado.append(s3[x])
    
    random.shuffle(resultado)
    senha = ''.join(resultado)
    print(f'Senha gerada: {senha}')


def senha_forte():
    #emabralhar tudo
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(quantidade_caracteres * (30/100))
    part2 = round(quantidade_caracteres * (20/100))

    resultado = []
    for x in range(part1):
        resultado.append(s1[x])
        resultado.append(s2[x])

    for x in range(part2):
        resultado.append(s3[x])
        resultado.append(s4[x])

    random.shuffle(resultado)
    senha = ''.join(resultado)
    print(f'Senha gerada: {senha}')


if escolha_usuario2 == 1:
    senha_basica()
elif escolha_usuario2 == 2:
    senha_forte()