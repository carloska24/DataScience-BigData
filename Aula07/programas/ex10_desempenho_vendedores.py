# Aula 07 - Exercício 10: Avaliação de desempenho de vendas com validação de metas
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 32)

'''
Enunciado:
Uma empresa deseja analisar o desempenho mensal de seus vendedores. Desenvolva um programa que solicite o nome de um vendedor, sua meta mensal e o valor total vendido.
O programa deverá calcular o percentual de atingimento da meta e classificar o desempenho:
- Abaixo de 80%: Abaixo da meta
- 80% até menos de 100%: Próximo da meta
- 100% até menos de 120%: Meta atingida
- 120% ou mais: Meta superada
Valide se a meta é maior que zero e se as vendas não são negativas.
'''

# 1. FUNÇÃO COM VALIDAÇÃO E CLASSIFICAÇÃO DE METAS
def avaliar_vendedor(nome: str, meta: float, vendas: float):
    # Validações exigidas no enunciado
    if meta <= 0:
        return None, "ERRO: A meta mensal deve ser estritamente maior que zero!"
    if vendas < 0:
        return None, "ERRO: O total de vendas não pode ser negativo!"
        
    percentual = (vendas / meta) * 100
    
    if percentual < 80.0:
        situacao = "Abaixo da meta"
    elif percentual < 100.0:
        situacao = "Próximo da meta"
    elif percentual < 120.0:
        situacao = "Meta atingida"
    else:
        situacao = "Meta superada"
        
    return {
        "vendedor": nome,
        "meta": meta,
        "vendas": vendas,
        "percentual": percentual,
        "situacao": situacao
    }, None

# 2. AVALIAÇÃO DA EQUIPE COMERCIAL
equipe = [
    ("Lucas Mendes", 50000.00, 35000.00),   # 70% (Abaixo da meta)
    ("Mariana Costa", 60000.00, 54000.00),  # 90% (Próximo da meta)
    ("Ricardo Alves", 40000.00, 44000.00),  # 110% (Meta atingida)
    ("Juliana Prado", 50000.00, 65000.00),  # 130% (Meta superada)
    ("Teste Inválido", -1000.00, 5000.00)   # Meta <= 0 (Erro)
]

print("=== RELATÓRIO MENSAL DE PERFORMANCE DE VENDAS ===")
for nome, meta, vendas in equipe:
    res, err = avaliar_vendedor(nome, meta, vendas)
    if err:
        print(f"{nome:15s} | {err}")
    else:
        print(f"{res['vendedor']:15s} | Meta: R$ {res['meta']:8.2f} | "
              f"Vendas: R$ {res['vendas']:8.2f} | Atingimento: {res['percentual']:6.1f}% | "
              f"Classificação: {res['situacao']}")

