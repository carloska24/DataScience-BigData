# Aula 07 - Exercício 17: Tabuada interativa de 1 a 10 com laço for
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 42)

'''
Enunciado:
2) Solicitar um número e apresentar sua tabuada de 1 a 10 utilizando for.
'''

# 1. FUNÇÃO DE GERAÇÃO DE TABUADA
def gerar_tabuada(numero: int):
    print(f"=== TABUADA DO NÚMERO {numero} ===")
    tabela = []
    for i in range(1, 11):
        resultado = numero * i
        tabela.append((i, resultado))
        print(f"{numero:2d} x {i:2d} = {resultado:3d}")
    return tabela

# 2. DEMONSTRAÇÃO COM NÚMEROS DE EXEMPLO
numero_escolhido = 7
tabuada_7 = gerar_tabuada(numero_escolhido)

# 3. TABUADA ADICIONAL (EX: BASE INDUSTRIAL / CÁLCULO DE PEÇAS)
print("\n=== APLICAÇÃO INDUSTRIAL: CÁLCULO DE LOTES (FATOR 12) ===")
gerar_tabuada(12)

