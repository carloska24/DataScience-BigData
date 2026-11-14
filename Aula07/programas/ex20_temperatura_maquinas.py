# Aula 07 - Exercício 20: Inspeção térmica de 10 máquinas: contagem em alerta e média
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 42)

'''
Enunciado:
5) solicitar a temperatura de 10 máquinas, contar quantas ultrapassaram 80 °C e calcular a temperatura média.
'''

# 1. LEITURA DE 10 MÁQUINAS INDUSTRIAIS
dados_inspecao = [
    ("Torno CNC 01", 68.5),
    ("Fresa 02", 74.0),
    ("Prensa Hidráulica 03", 85.0), # Alerta
    ("Compressor A 04", 62.0),
    ("Injetora 05", 91.5),          # Alerta
    ("Retificadora 06", 58.0),
    ("Centro de Usinagem 07", 83.2), # Alerta
    ("Torno Convencional 08", 45.0),
    ("Esteira Transportadora 09", 52.0),
    ("Solda Robotizada 10", 88.0)   # Alerta
]

# 2. PROCESSAMENTO COM LAÇO FOR
soma_temperaturas = 0.0
maquinas_em_alerta = 0
lista_alertas = []

print("=== INSPEÇÃO TÉRMICA DE 10 MÁQUINAS INDUSTRIAIS ===")
for i, (nome, temp) in enumerate(dados_inspecao, start=1):
    soma_temperaturas += temp
    em_alerta = temp > 80.0
    if em_alerta:
        maquinas_em_alerta += 1
        lista_alertas.append((nome, temp))
        aviso = "🔥 ALERTA (> 80 °C)"
    else:
        aviso = "✅ NORMAL"
    print(f"Máquina {i:2d}: {nome:25s} | Temperatura: {temp:5.1f} °C | Status: {aviso}")

# 3. CÁLCULO DA MÉDIA E RELATÓRIO CONSOLIDADO
media_temperatura = soma_temperaturas / len(dados_inspecao)

print("\n=== RELATÓRIO CONSOLIDADO DA MANUTENÇÃO ===")
print(f"Total de máquinas inspecionadas: {len(dados_inspecao)}")
print(f"Temperatura média do parque: {media_temperatura:.1f} °C")
print(f"Quantidade de máquinas acima de 80 °C: {maquinas_em_alerta} ({maquinas_em_alerta/len(dados_inspecao)*100:.0f}%)")
print("\nMáquinas que necessitam de intervenção imediata:")
for m, t in lista_alertas:
    print(f" -> {m} com {t:.1f} °C")

