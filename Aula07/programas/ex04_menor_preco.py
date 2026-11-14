# Aula 07 - Exercício 04: Menor preço entre três produtos
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 26)

'''
Enunciado:
Escreva um programa que pergunte o preço de três produtos e indique qual o produto com menor preço.
'''

# 1. COTACÕES DOS PRODUTOS
produtos = {
    "Produto A (Fornecedor 1)": 45.90,
    "Produto B (Fornecedor 2)": 38.50,
    "Produto C (Fornecedor 3)": 52.00
}

# 2. LOCALIZAÇÃO DO PRODUTO MAIS ECONÔMICO
menor_produto = None
menor_valor = float("inf")

for nome, preco in produtos.items():
    if preco < menor_valor:
        menor_valor = preco
        menor_produto = nome

# 3. RELATÓRIO DE COMPRA
print("=== COTAÇÃO DE FORNECEDORES ===")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nRecomendação de Compra:")
print(f"-> Escolha: {menor_produto} pelo menor valor de R$ {menor_valor:.2f}.")

