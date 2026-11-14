# Aula 07 - Exercício 09: Consumo energético e classificação de máquinas industriais
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 31)

'''
Enunciado:
Uma empresa deseja identificar o nível de consumo energético de suas máquinas. Solicite o nome da máquina, sua potência em kW e a quantidade de horas de funcionamento.
Calcule o consumo: Consumo (kWh) = Potência (kW) × Horas.
Classifique o resultado conforme faixas didáticas:
- Menos de 100 kWh: Baixo consumo.
- De 100 até menos de 300 kWh: Consumo moderado.
- 300 kWh ou mais: Alto consumo.
'''

# 1. FUNÇÃO DE CÁLCULO E CLASSIFICAÇÃO ENERGÉTICA
def classificar_consumo(nome: str, potencia_kw: float, horas: float):
    consumo_kwh = potencia_kw * horas
    
    if consumo_kwh < 100.0:
        categoria = "Baixo consumo"
    elif consumo_kwh < 300.0:
        categoria = "Consumo moderado"
    else:
        categoria = "Alto consumo"
        
    return {
        "maquina": nome,
        "potencia_kw": potencia_kw,
        "horas": horas,
        "consumo_kwh": consumo_kwh,
        "categoria": categoria
    }

# 2. AUDITORIA EM LINHA DE PRODUÇÃO
parque_maquinas = [
    ("Furadeira de Bancada", 1.5, 8.0),     # 12 kWh (Baixo)
    ("Torno Mecânico", 15.0, 12.0),         # 180 kWh (Moderado)
    ("Prensa Hidráulica", 45.0, 16.0),      # 720 kWh (Alto)
    ("Compressor Industrial", 25.0, 10.0)   # 250 kWh (Moderado)
]

print("=== AUDITORIA DE CONSUMO ENERGÉTICO INDUSTRIAL ===")
for m, p, h in parque_maquinas:
    res = classificar_consumo(m, p, h)
    print(f"Máquina: {res['maquina']:22s} | Potência: {res['potencia_kw']:4.1f} kW | "
          f"Horas: {res['horas']:4.1f} h | Consumo: {res['consumo_kwh']:6.1f} kWh | Faixa: {res['categoria']}")

