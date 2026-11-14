# Aula 07 - Exercício 06: Variação de vendas imobiliárias e diretrizes de gestão
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 28)

'''
Enunciado:
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual:
- Acima de 20%: bonificação para o time de vendas.
- Entre 2% e 20%: pequena bonificação para time de vendas.
- Entre 2% e -10%: planejamento de políticas de incentivo às vendas.
- Abaixo de -10%: corte de gastos.
'''

# 1. FUNÇÃO DE ANÁLISE DE VENDAS
def analisar_desempenho_imoveis(vendas_2022: int, vendas_2023: int):
    if vendas_2022 <= 0:
        return None, "Vendas de 2022 devem ser maiores que zero."
    
    variacao_pct = ((vendas_2023 - vendas_2022) / vendas_2022) * 100
    
    if variacao_pct > 20.0:
        sugestao = "Bonificação para o time de vendas."
    elif 2.0 <= variacao_pct <= 20.0:
        sugestao = "Pequena bonificação para time de vendas."
    elif -10.0 <= variacao_pct < 2.0:
        sugestao = "Planejamento de políticas de incentivo às vendas."
    else:
        sugestao = "Corte de gastos."
        
    return {
        "v2022": vendas_2022,
        "v2023": vendas_2023,
        "variacao_pct": variacao_pct,
        "sugestao": sugestao
    }, None

# 2. CENÁRIOS DE FILIAIS DA IMOBILIÁRIA
filiais = [
    ("Filial Norte", 100, 125),   # +25% (> 20%)
    ("Filial Sul", 200, 218),     # +9% (2% a 20%)
    ("Filial Leste", 150, 148),   # -1.33% (-10% a 2%)
    ("Filial Oeste", 180, 150)    # -16.67% (< -10%)
]

print("=== AVALIAÇÃO DE DESEMPENHO DAS FILIAIS ===")
for nome, v22, v23 in filiais:
    res, _ = analisar_desempenho_imoveis(v22, v23)
    print(f"{nome:14s} | 2022: {v22:3d} un | 2023: {v23:3d} un | Variação: {res['variacao_pct']:+6.2f}% | Decisão: {res['sugestao']}")

