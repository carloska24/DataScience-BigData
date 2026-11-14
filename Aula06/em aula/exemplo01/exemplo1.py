import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "maquina": ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"],
    "consumo": [120, 150, 100, 200, 250, 300, 350, 400, 450, 500]
}

df = pd.DataFrame(dados)

df.plot(
    x="maquina",
    y="consumo",
    kind="bar",
    legend=False
)

plt.title("Consumo energético por máquina")
plt.ylabel("Consumo (kWh)")
plt.show()
