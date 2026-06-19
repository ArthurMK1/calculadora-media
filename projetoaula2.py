#VERSIONAMENTO git
alunos = []
notas = []
medias = []
while True:
    aluno = input("Qual o nome do Aluno: ")
    alunos.append(aluno)

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    notas.append([nota1, nota2, nota3])

    media = (nota1 + nota2 + nota3) / 3
    medias.append(media)

    op = input("Você deseja continuar? (s/n) ")
    if (op == "n"):
        break
    
print("\n====RELATORIO====")
for i in range(len(alunos)):
    print(f"\nAluno(a): {alunos[i]}")
    print(f"As notas do(a) aluno(a) foram: {notas[i][0]}, {notas[i][1]}, {notas[i][2]}")
    print(f"E a média do(a) aluno(a) foi: {medias[i]:.2f}")

    if medias[i] >= 7:
        status = "Aprovado"
    elif medias[i] >= 5: 
        status = "Recuperação"
    else:
        status = "Reprovado"

    print(f"STATUS: {status}")
