# Monitoramento da temperatura de uma máquina
# Aluno: Carlos Alexandre Duarte Pereira
# Fonte: Aula 01 - Python para Data Science, páginas 37 a 39.

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt

# 2. CRIAÇÃO DO DATAFRAME
dados = {
    "tempo": ["08:00", "09:00", "10:00", "11:00", "12:00",
              "13:00", "14:00", "15:00", "16:00", "17:00"],
    "temperatura": [25, 28, 32, 35, 38, 42, 45, 41, 37, 33]
}
df = pd.DataFrame(dados)
print(df)

# 3. GRÁFICO DE LINHAS
plt.figure(figsize=(10, 5))
plt.plot(df["tempo"], df["temperatura"], marker="o", color="tab:orange")
plt.title("Variação da temperatura da máquina")
plt.xlabel("Horário")
plt.ylabel("Temperatura (°C)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# a) Em qual horário foi registrada a maior temperatura?

temperatura_maxima = df["temperatura"].max()
print(df.loc[df["temperatura"] == temperatura_maxima, ["tempo", "temperatura"]])

# b) Qual foi a menor temperatura registrada?

temperatura_minima = df["temperatura"].min()
print(f"Menor temperatura: {temperatura_minima} °C")

# c) Em qual intervalo ocorreu a maior elevação de temperatura?

# diff() calcula a diferença entre uma leitura e a anterior.
# shift() coloca o horário anterior ao lado do horário atual.
df["variacao_temperatura"] = df["temperatura"].diff()
intervalos = pd.DataFrame({
    "horario_inicial": df["tempo"].shift(1),
    "horario_final": df["tempo"],
    "elevacao_c": df["variacao_temperatura"]
}).dropna()
maior_elevacao = intervalos["elevacao_c"].max()
print(intervalos)
print("Intervalos com a maior elevação:")
print(intervalos.loc[intervalos["elevacao_c"] == maior_elevacao])

# d) Como calcular a temperatura média utilizando df["temperatura"].mean()?

temperatura_media = df["temperatura"].mean()
print(f"Temperatura média: {temperatura_media:.1f} °C")
