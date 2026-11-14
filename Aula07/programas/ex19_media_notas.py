# Aula 07 - Exercício 19: Cálculo da média da turma com repetição e notas de alunos
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 42)

'''
Enunciado:
4) solicitar as notas de 5 alunos e calcular a média da turma.
'''

# 1. LISTA DE ALUNOS E NOTAS
alunos = ["Carlos", "Mariana", "Pedro", "Juliana", "Rafael"]
notas = [8.5, 7.0, 9.2, 6.8, 8.0]

# 2. ITERAÇÃO PARA SOMA DAS NOTAS
soma_notas = 0.0
print("=== REGISTRO DE NOTAS DOS ALUNOS ===")
for aluno, nota in zip(alunos, notas):
    soma_notas += nota
    status_individual = "Aprovado" if nota >= 7.0 else "Recuperação"
    print(f"Aluno: {aluno:10s} | Nota: {nota:4.1f} | Situação: {status_individual}")

# 3. CÁLCULO DA MÉDIA DA TURMA
media_turma = soma_notas / len(notas)

print("\n=== DESEMPENHO GERAL DA TURMA ===")
print(f"Total de alunos avaliados: {len(alunos)}")
print(f"Soma das notas: {soma_notas:.1f}")
print(f"Média da turma: {media_turma:.2f}")

if media_turma >= 7.0:
    print("Classificação da Turma: Desempenho Satisfatório (Média >= 7.0)")
else:
    print("Classificação da Turma: Desempenho Insatisfatório (Necessita reforço)")

