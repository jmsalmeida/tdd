notas = []

i = 0
j = 0
acumulador = 0

while i < 4:
    i += 1
    nota_inserida = float(input(str("Entre com a nota ") + str(i) + str(" do aluno:  ")))
    notas.append(nota_inserida)

while j < 4:
    acumulador += notas[j]
    j += 1

media = acumulador/4

if media >= 7:
    print("O aluno foi aprovado com a média", media)
elif media < 7 and media >= 5.5:
    print("O aluno ficou para recuperação com a média", media)
else:
    print("O aluno reprovado com a média", media)
