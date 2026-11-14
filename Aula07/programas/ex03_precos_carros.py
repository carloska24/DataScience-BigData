# Aula 07 - Exercício 03: Preços médios de modelo automotivo por 3 anos
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 26)

'''
Enunciado:
Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
'''

# 1. DADOS DE PREÇOS MÉDIOS DO VEÍCULO (3 ANOS)
anos = [2024, 2025, 2026]
precos = [85400.00, 92800.00, 88200.00]

# 2. DETERMINAÇÃO DO MAIOR E MENOR PREÇO VIA CONDICIONAIS
maior_preco = precos[0]
ano_maior = anos[0]
menor_preco = precos[0]
ano_menor = anos[0]

for ano, preco in zip(anos[1:], precos[1:]):
    if preco > maior_preco:
        maior_preco = preco
        ano_maior = ano
    if preco < menor_preco:
        menor_preco = preco
        ano_menor = ano

# 3. EXIBIÇÃO DOS RESULTADOS
print("=== HISTÓRICO DE PREÇOS MÉDIOS DO VEÍCULO ===")
for ano, p in zip(anos, precos):
    print(f"Ano {ano}: R$ {p:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

print("\n=== EXTREMOS IDENTIFICADOS ===")
print(f"Maior preço médio: R$ {maior_preco:,.2f} (Ano {ano_maior})".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Menor preço médio: R$ {menor_preco:,.2f} (Ano {ano_menor})".replace(",", "X").replace(".", ",").replace("X", "."))

