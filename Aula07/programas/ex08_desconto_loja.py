# Aula 07 - Exercício 08: Descontos progressivos por faixa de valor de compra
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 30)

'''
Enunciado:
Uma loja oferece descontos de acordo com o valor total da compra. Solicite o nome do cliente e o valor da compra:
- Abaixo de R$ 100: 0%
- De R$ 100 até menos de R$ 500: 5%
- De R$ 500 até menos de R$ 1.000: 10%
- R$ 1.000 ou mais: 15%
'''

# 1. FUNÇÃO DE CÁLCULO DE DESCONTO EM COMPRAS
def calcular_desconto_compra(nome: str, valor: float):
    if valor < 0:
        return None, "Valor da compra não pode ser negativo."
    
    if valor < 100.00:
        pct_desconto = 0.00
    elif valor < 500.00:
        pct_desconto = 0.05
    elif valor < 1000.00:
        pct_desconto = 0.10
    else:
        pct_desconto = 0.15
        
    valor_desconto = valor * pct_desconto
    valor_final = valor - valor_desconto
    
    return {
        "cliente": nome,
        "valor_original": valor,
        "pct_desconto": pct_desconto * 100,
        "valor_desconto": valor_desconto,
        "valor_final": valor_final
    }, None

# 2. CENÁRIOS DE CLIENTES EM CADA FAIXA
clientes_teste = [
    ("Ana Souza", 80.00),     # < 100 (0%)
    ("Bruno Lima", 250.00),   # 100 a < 500 (5%)
    ("Carla Dias", 750.00),   # 500 a < 1000 (10%)
    ("Daniel Silva", 1400.00) # >= 1000 (15%)
]

print("=== NOTA DE VENDA COM DESCONTO ===")
for c, v in clientes_teste:
    res, _ = calcular_desconto_compra(c, v)
    print(f"Cliente: {res['cliente']:13s} | Compra: R$ {res['valor_original']:7.2f} | "
          f"Desconto: {res['pct_desconto']:2.0f}% (R$ {res['valor_desconto']:6.2f}) | "
          f"Total a Pagar: R$ {res['valor_final']:7.2f}")

