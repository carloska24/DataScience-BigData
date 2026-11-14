# Aula 07 - Exercício 13: Controle de acesso e autenticação de usuários (Operador AND)
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 34)

'''
Enunciado:
Solicite o nome de usuário e a senha. Permita o acesso apenas quando o usuário for 'admin' e a senha for '1234'.
'''

# 1. FUNÇÃO DE AUTENTICAÇÃO
def autenticar(usuario: str, senha: str) -> bool:
    # Exige que ambas as condições sejam simultaneamente verdadeiras
    return (usuario == "admin") and (senha == "1234")

# 2. SIMULAÇÃO DE TENTATIVAS DE ACESSO
tentativas = [
    ("admin", "1234"),    # Ambas corretas (True and True -> True)
    ("admin", "9999"),    # Senha incorreta (True and False -> False)
    ("convidado", "1234"),# Usuário incorreto (False and True -> False)
    ("root", "toor")      # Ambas incorretas (False and False -> False)
]

print("=== SISTEMA DE LOGIN E SEGURANÇA ===")
for u, s in tentativas:
    sucesso = autenticar(u, s)
    if sucesso:
        print(f"Usuário: '{u:10s}' | Senha: '{s:5s}' -> ACESSO PERMITIDO! Bem-vindo ao painel.")
    else:
        print(f"Usuário: '{u:10s}' | Senha: '{s:5s}' -> ACESSO NEGADO! Credenciais inválidas.")

