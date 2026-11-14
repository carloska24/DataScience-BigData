# Aula 07 - Exercício 05: Cálculo de abastecimento e descontos em combustíveis
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 27)

'''
Enunciado:
Um estabelecimento está vendendo combustíveis com descontos variados:
- Etanol (E): R$ 1,70/litro. Se litros >= 15, desconto de 4% por litro. Senão, 3% por litro.
- Diesel (D): R$ 2,00/litro. Se litros >= 15, desconto de 5% por litro. Senão, 3% por litro.
- Gasolina (G): R$ 4,50/litro. Se litros >= 20, desconto de 3% por litro. Senão, sem desconto.
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E, D, G) e calcule o valor a ser pago pelo cliente.
'''

# 1. FUNÇÃO DE CÁLCULO DE COMBUSTÍVEL
def calcular_combustivel(tipo: str, litros: float):
    tipo = tipo.upper().strip()
    
    if tipo == "E":
        nome = "Etanol"
        preco_litro = 1.70
        taxa_desconto = 0.04 if litros >= 15 else 0.03
    elif tipo == "D":
        nome = "Diesel"
        preco_litro = 2.00
        taxa_desconto = 0.05 if litros >= 15 else 0.03
    elif tipo == "G":
        nome = "Gasolina"
        preco_litro = 4.50
        taxa_desconto = 0.03 if litros >= 20 else 0.00
    else:
        return None, "Tipo de combustível inválido! Use E, D ou G."
    
    valor_bruto = preco_litro * litros
    valor_desconto = valor_bruto * taxa_desconto
    valor_final = valor_bruto - valor_desconto
    
    return {
        "tipo": tipo,
        "nome": nome,
        "litros": litros,
        "preco_litro": preco_litro,
        "taxa_desconto_pct": taxa_desconto * 100,
        "valor_bruto": valor_bruto,
        "valor_desconto": valor_desconto,
        "valor_final": valor_final
    }, None

# 2. SIMULAÇÃO DE CENÁRIOS
simulacoes = [
    ("E", 10.0),  # Etanol < 15L (3%)
    ("E", 25.0),  # Etanol >= 15L (4%)
    ("D", 12.0),  # Diesel < 15L (3%)
    ("D", 40.0),  # Diesel >= 15L (5%)
    ("G", 15.0),  # Gasolina < 20L (0%)
    ("G", 30.0),  # Gasolina >= 20L (3%)
]

print("=== RELATÓRIO DE ABASTECIMENTOS ===")
for t, l in simulacoes:
    res, err = calcular_combustivel(t, l)
    if res:
        print(f"Combustível: {res['nome']:8s} | Litros: {res['litros']:4.1f} L | "
              f"Bruto: R$ {res['valor_bruto']:6.2f} | Desc: {res['taxa_desconto_pct']:3.1f}% (R$ {res['valor_desconto']:5.2f}) | "
              f"Total a Pagar: R$ {res['valor_final']:6.2f}")

