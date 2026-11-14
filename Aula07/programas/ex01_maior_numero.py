# Aula 07 - Exercício 01: Maior entre dois números
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 26)

'''
Enunciado:
Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
'''

# 1. DEFINIÇÃO DA LÓGICA DE COMPARAÇÃO
def identificar_maior(num1: float, num2: float):
    """Compara dois números e retorna o maior valor ou indica igualdade."""
    if num1 > num2:
        return f"O primeiro número ({num1}) é MAIOR que o segundo ({num2})."
    elif num2 > num1:
        return f"O segundo número ({num2}) é MAIOR que o primeiro ({num1})."
    else:
        return f"Os dois números são IGUAIS ({num1} = {num2})."

# 2. DEMONSTRAÇÃO COM DIFERENTES CENÁRIOS INDUSTRIAIS
casos_de_teste = [
    (45.5, 78.2),   # Segundo maior
    (120.0, 95.4),  # Primeiro maior
    (30.0, 30.0),   # Iguais
    (-15.2, -5.0)   # Números negativos
]

print("=== RESULTADOS DOS TESTES AUTOMATIZADOS ===")
for a, b in casos_de_teste:
    resultado = identificar_maior(a, b)
    print(f"Comparando {a} e {b} -> {resultado}")

# 3. MODO INTERATIVO (Exemplo com dados simulados / teclado)
def executar_interativo():
    print("\n=== EXECUÇÃO INTERATIVA ===")
    try:
        # Valores simulados caso executado sem terminal interativo
        entrada1 = "84.5"
        entrada2 = "62.1"
        n1 = float(entrada1.replace(",", "."))
        n2 = float(entrada2.replace(",", "."))
        print(f"Número 1 informado: {n1}")
        print(f"Número 2 informado: {n2}")
        print("Resultado:", identificar_maior(n1, n2))
    except ValueError:
        print("Erro: digite valores numéricos válidos.")

executar_interativo()

