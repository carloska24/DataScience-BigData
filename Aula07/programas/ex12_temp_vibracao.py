# Aula 07 - Exercício 12: Alerta preditivo de temperatura ou vibração (Operador OR)
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 34)

'''
Enunciado:
Um sistema monitora a temperatura e a vibração de uma máquina industrial. Criar um programa para permitir que o usuário digite a temperatura e o sistema emita um alerta quando a temperatura ultrapassar 80 °C ou a vibração ultrapassar 15 mm/s.
'''

# 1. FUNÇÃO DE MONITORAMENTO COM OPERADOR OR
def verificar_maquina_temp_vib(temp_c: float, vibracao_mms: float):
    # Condição lógica: temperatura > 80 OU vibração > 15
    emite_alerta = (temp_c > 80.0) or (vibracao_mms > 15.0)
    
    if emite_alerta:
        status = "ALERTA EMITIDO: Condições fora dos limites de segurança!"
    else:
        status = "Operação Normal: Sensores dentro dos padrões tolerados."
        
    return {
        "temperatura": temp_c,
        "vibracao": vibracao_mms,
        "alerta": emite_alerta,
        "status": status
    }

# 2. TESTES DA TABELA-VERDADE DO OPERADOR OR
cenarios = [
    (65.0, 8.0),   # Ambas normais (False or False -> False)
    (88.0, 10.0),  # Temp alta, Vib normal (True or False -> True)
    (70.0, 18.5),  # Temp normal, Vib alta (False or True -> True)
    (92.0, 22.0)   # Ambas altas (True or True -> True)
]

print("=== ANÁLISE DE SENSORES CONJUNTOS (OR) ===")
for t, v in cenarios:
    r = verificar_maquina_temp_vib(t, v)
    simbolo = "🔴" if r["alerta"] else "🟢"
    print(f"{simbolo} Temp: {t:4.1f} °C | Vibração: {v:4.1f} mm/s -> {r['status']}")

