# 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foio maior e o menor peso lidos.

"""maior = 200
menor = 0


for c in range(0, 5):
    peso = int(input('Digite seu peso: '))

    if peso < maior:
        maior = peso
    if peso > menor:
        menor = peso

print(f'o maior peso foi {menor} e o menor peso foi {maior}')"""

# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

# tabuada = int(input('Digite o número que deseja a tabuada: '))

# for c in range(10):
#     print("%d x %d = %d" % (tabuada, c+1, tabuada*(c+1)))

# 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# menor = 0
# maior = 0
# for c in range(7):
#     idade = int(input('Digite sua idade: '))

#     if idade < 18:
#         menor += 1
#     if idade > 18:
#         maior += 1
# print(f'{maior} já são maiores de idade,  e {menor} ainda são menores de idade!')

# 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

# par = 0
# qpar = 0

# for c in range(6):
#     num = int(input('Digite um número: '))

#     if num % 2 == 0:
#         par += num
#     if num % 2 == 0:
#         qpar += 1
# print(
#     f'A soma dos números pares é: {par}! E a quantidade de números pares inseridos são: {qpar}')

"""#01 - Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
sem break)"""