# Aula 07 - Exercício 02: Percentual de crescimento da produção
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 26)

'''
Enunciado:
Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou um decrescimento (porcentagem negativa).
'''

# 1. FUNÇÃO DE CLASSIFICAÇÃO DA PRODUÇÃO
def avaliar_crescimento(percentual: float) -> str:
    """Classifica a variação da produção conforme o sinal do percentual."""
    if percentual > 0:
        return f"Crescimento na produção: aumento de +{percentual:.2f}%."
    elif percentual < 0:
        return f"Decrescimento na produção: queda de {percentual:.2f}%."
    else:
        return "Estabilidade na produção: variação nula (0.00%)."

# 2. TESTES COM DADOS INDUSTRIAIS HISTÓRICOS
historico_meses = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"],
    "Percentual (%)": [12.5, -4.8, 0.0, 8.3, -15.2]
}

print("=== ANÁLISE DE HISTÓRICO DE PRODUÇÃO ===")
for mes, pct in zip(historico_meses["Mês"], historico_meses["Percentual (%)"]):
    resultado = avaliar_crescimento(pct)
    print(f"{mes:10s} | Taxa: {pct:+6.2f}% -> {resultado}")

