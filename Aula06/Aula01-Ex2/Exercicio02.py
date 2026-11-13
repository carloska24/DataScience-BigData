# Análise de vendas por setor e cliente
# Aluno: Carlos Alexandre Duarte Pereira
# Fonte: Aula 01 - Python para Data Science, páginas 40 a 42.

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt

# 2. CRIAÇÃO DO DATAFRAME
dados = {
    "cliente": ["C1", "C2", "C3", "C4", "C5",
                "C6", "C7", "C8", "C9", "C10"],
    "setor": ["Tecnologia", "Indústria", "Comércio",
              "Tecnologia", "Indústria", "Comércio",
              "Tecnologia", "Indústria", "Comércio", "Tecnologia"],
    "vendas": [1500, 2500, 1200, 3000, 4500,
               2000, 3500, 5000, 2800, 4000]
}
df = pd.DataFrame(dados)
print(df)

# 3. FATURAMENTO TOTAL POR SETOR
faturamento_setor = df.groupby("setor")["vendas"].sum().sort_values(ascending=False)
print(faturamento_setor.to_frame("faturamento_total_rs"))

# 4. GRÁFICO DE BARRAS
ax = faturamento_setor.plot(kind="bar", figsize=(9, 5), color="tab:blue", rot=0)
for posicao, valor in enumerate(faturamento_setor):
    ax.text(posicao, valor + 150, f"R$ {valor:,.0f}".replace(",", "."), ha="center")
ax.set_title("Faturamento total por setor")
ax.set_xlabel("Setor")
ax.set_ylabel("Faturamento (R$)")
ax.set_ylim(0, faturamento_setor.max() * 1.15)
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()

# a) Qual setor apresentou o maior faturamento?

maior_faturamento = faturamento_setor.max()
# O filtro retorna todos os setores empatados no maior valor.
print(faturamento_setor.loc[faturamento_setor == maior_faturamento].to_frame("faturamento_total_rs"))

# b) Qual setor apresentou o menor faturamento?

menor_faturamento = faturamento_setor.min()
print(faturamento_setor.loc[faturamento_setor == menor_faturamento].to_frame("faturamento_total_rs"))

# c) Qual cliente realizou a compra de maior valor?

maior_venda = df["vendas"].max()
print(df.loc[df["vendas"] == maior_venda, ["cliente", "setor", "vendas"]])

# d) Como calcular o faturamento total da empresa utilizando df["vendas"].sum()?

faturamento_total = df["vendas"].sum()
print("Faturamento total: R$", f"{faturamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# e) Como calcular a média das vendas por setor utilizando groupby() e mean()?

media_setor = df.groupby("setor")["vendas"].mean()
print(media_setor.to_frame("media_vendas_rs"))
