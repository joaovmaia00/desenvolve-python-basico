
# Lê o valor inteiro em reais
valor = int(input())

# Calcula a quantidade de notas de 100 reais
notas100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50 reais
notas50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20 reais
notas20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10 reais
notas10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5 reais
notas5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2 reais
notas2 = valor // 2
valor = valor % 2

# Calcula a quantidade de notas de 1 real
notas1 = valor

# Imprime a quantidade de cada nota no formato solicitado
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")
