# Aula 07 - Exercício 15: Monitoramento de temperatura e umidade crítica (Operador AND)
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 34)

'''
Enunciado:
Solicite a temperatura e a umidade de um ambiente industrial. Exiba um alerta quando a temperatura ultrapassar 35 °C e a umidade estiver abaixo de 30%.
'''

# 1. FUNÇÃO DE MONITORAMENTO AMBIENTAL
def monitorar_clima_industrial(temperatura_c: float, umidade_pct: float):
    # Condição crítica: temperatura > 35 E umidade < 30
    alerta_critico = (temperatura_c > 35.0) and (umidade_pct < 30.0)
    
    if alerta_critico:
        diagnostico = "ALERTA CRÍTICO: Ambiente quente e seco! Risco de sobreaquecimento e eletricidade estática."
    else:
        diagnostico = "Ambiente dentro dos parâmetros normais de trabalho."
        
    return {
        "temperatura": temperatura_c,
        "umidade": umidade_pct,
        "alerta": alerta_critico,
        "diagnostico": diagnostico
    }

# 2. LEITURAS EM DIFERENTES GALPÕES
leituras = [
    (28.0, 55.0),  # Agradável (False and False)
    (38.0, 45.0),  # Quente, mas úmido (True and False)
    (30.0, 22.0),  # Frio/ameno, mas seco (False and True)
    (39.5, 18.0)   # Quente e muito seco (True and True -> ALERTA)
]

print("=== CONTROLE METEOROLÓGICO INDUSTRIAL (AND) ===")
for t, u in leituras:
    res = monitorar_clima_industrial(t, u)
    simbolo = "🔥 ALERTA" if res['alerta'] else "✅ NORMAL"
    print(f"Temp: {t:4.1f} °C | Umidade: {u:4.1f}% | {simbolo:10s} -> {res['diagnostico']}")

