# Aula 07 - Exercício 11: Monitoramento térmico de máquinas e alerta crítico
# Aluno: Carlos Alexandre Duarte Pereira
# Disciplina: Python para Data Science | Prof. Me. Daniel Vieira
# Fonte: Aula 02 - Python para Data Science.pdf (página 33)

'''
Enunciado:
Uma indústria utiliza sensores para monitorar a temperatura de suas máquinas. Desenvolva um programa que solicite o nome da máquina e sua temperatura atual em graus Celsius. Utilize estruturas condicionais para determinar o estado operacional:
- Abaixo de 40 °C: Operação normal
- De 40 °C até menos de 60 °C: Atenção
- De 60 °C até 80 °C: Alerta de aquecimento
- Acima de 80 °C: Temperatura crítica
Caso a temperatura seja crítica, apresente a mensagem: 'ALERTA: verificar imediatamente a máquina!'
'''

# 1. FUNÇÃO DE MONITORAMENTO TÉRMICO
def monitorar_temperatura(nome_maquina: str, temp_c: float):
    if temp_c < 40.0:
        estado = "Operação normal"
        alerta_critico = False
    elif temp_c < 60.0:
        estado = "Atenção"
        alerta_critico = False
    elif temp_c <= 80.0:
        estado = "Alerta de aquecimento"
        alerta_critico = False
    else:
        estado = "Temperatura crítica"
        alerta_critico = True
        
    mensagem_alerta = "ALERTA: verificar imediatamente a máquina!" if alerta_critico else "Sem pendências de emergência."
    
    return {
        "maquina": nome_maquina,
        "temperatura": temp_c,
        "estado": estado,
        "critico": alerta_critico,
        "mensagem": mensagem_alerta
    }

# 2. LEITURA DOS SENSORES EM TEMPO REAL
sensores = [
    ("Bomba Centrífuga 01", 32.5),   # < 40
    ("Injetora Plástica 02", 48.0),  # 40 a < 60
    ("Extrusora 03", 72.0),          # 60 a 80
    ("Motor Principal 04", 94.5)     # > 80 (Crítica)
]

print("=== QUADRO DE CONTROLE DE TEMPERATURA FABRIL ===")
for maq, t in sensores:
    res = monitorar_temperatura(maq, t)
    print(f"Máquina: {res['maquina']:22s} | Temp: {res['temperatura']:5.1f} °C | Estado: {res['estado']:22s}")
    if res['critico']:
        print(f"   >>> {res['mensagem']}")

