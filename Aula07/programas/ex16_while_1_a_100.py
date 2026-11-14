# Aula 07 - Exercício 16: Contagem sequencial de 1 a 100 com estrutura while
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 42)

'''
Enunciado:
1) Mostrar os números de 1 a 100 utilizando while
'''

# 1. INICIALIZAÇÃO DA VARIÁVEL DE CONTROLE
contador = 1
numeros = []

# 2. ESTRUTURA WHILE DE REPETIÇÃO
while contador <= 100:
    numeros.append(contador)
    contador += 1  # Incremento fundamental para encerramento do laço

# 3. EXIBIÇÃO FORMATADA DOS NÚMEROS (EM BLOCOS DE 10 PARA LEITURA CLARA)
print("=== CONTAGEM DE 1 A 100 COM WHILE ===")
for i in range(0, 100, 10):
    linha = " ".join(f"{num:3d}" for num in numeros[i:i+10])
    print(linha)

print(f"\nContador final após o loop: {contador}")
print(f"Total de números gerados: {len(numeros)}")

