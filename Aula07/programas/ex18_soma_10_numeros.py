# Aula 07 - Exercício 18: Acumulador numérico e somatório de 10 valores
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 42)

'''
Enunciado:
3) solicitar 10 números e calcular a soma total.
'''

# 1. DADOS DE ENTRADA (10 VALORES COLETADOS)
valores = [15.2, 22.8, 18.0, 35.4, 42.1, 19.5, 27.3, 31.0, 14.9, 25.8]

# 2. CÁLCULO DA SOMA COM LAÇO FOR E ACUMULADOR
soma_total = 0.0
print("=== PROCESSAMENTO DOS 10 NÚMEROS ===")
for i, valor in enumerate(valores, start=1):
    soma_total += valor
    print(f"Passo {i:2d} | Valor recebido: {valor:5.1f} | Soma parcial: {soma_total:6.1f}")

media_valores = soma_total / len(valores)

# 3. RELATÓRIO ESTATÍSTICO
print("\n=== RESULTADO FINAL ===")
print(f"Quantidade de números processados: {len(valores)}")
print(f"Soma total acumulada: {soma_total:.2f}")
print(f"Média aritmética dos valores: {media_valores:.2f}")
print(f"Maior valor da série: {max(valores):.2f}")
print(f"Menor valor da série: {min(valores):.2f}")

