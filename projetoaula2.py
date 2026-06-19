#VERSIONAMENTO git
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("ALUNO APROVADO!!!")
else: 
    print("O aluno foi reprovado")

print(media)
