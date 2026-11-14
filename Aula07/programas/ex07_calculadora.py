# Aula 07 - Exercício 07: Calculadora aritmética com tratamento de divisão por zero
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 29)

'''
Enunciado:
Desenvolva um programa que solicite dois números e uma operação matemática (+, -, * ou /). Utilize estruturas condicionais para identificar a operação e apresentar o resultado. Caso o usuário escolha uma divisão por zero, exiba uma mensagem de erro.
'''

# 1. FUNÇÃO DA CALCULADORA
def calcular(num1: float, num2: float, operacao: str):
    operacao = operacao.strip()
    
    if operacao == "+":
        return num1 + num2, None
    elif operacao == "-":
        return num1 - num2, None
    elif operacao == "*":
        return num1 * num2, None
    elif operacao == "/":
        if num2 == 0:
            return None, "ERRO: Divisão por zero não é permitida!"
        return num1 / num2, None
    else:
        return None, f"ERRO: Operação '{operacao}' inválida! Escolha +, -, * ou /."

# 2. TESTES DE TODAS AS OPERAÇÕES E CASOS ESPECIAIS
testes = [
    (15, 3, "+"),
    (20, 7, "-"),
    (6, 8, "*"),
    (48, 6, "/"),
    (10, 0, "/"),  # Divisão por zero
    (5, 2, "%")    # Operador desconhecido
]

print("=== DEMONSTRAÇÃO DA CALCULADORA ===")
for n1, n2, op in testes:
    res, err = calcular(n1, n2, op)
    if err:
        print(f"{n1} {op} {n2} -> {err}")
    else:
        print(f"{n1} {op} {n2} = {res:.2f}")

