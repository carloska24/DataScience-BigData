# Evolução dos preços de fechamento de ações
# Aluno: Carlos Alexandre Duarte Pereira
# Fonte: Aula 01 - Python para Data Science, páginas 43 a 45.

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt

# 2. CRIAÇÃO DO DATAFRAME
dados = {
    "dia": ["D1", "D2", "D3", "D4", "D5",
            "D6", "D7", "D8", "D9", "D10"],
    "preco": [25.50, 26.20, 25.80, 27.00, 28.50,
              27.80, 29.20, 30.50, 29.80, 31.00]
}
df = pd.DataFrame(dados)
print(df)

# 3. GRÁFICO DE LINHAS
# Mantém a ordem D1 a D10 fornecida no enunciado.
plt.figure(figsize=(10, 5))
plt.plot(df["dia"], df["preco"], marker="o", color="tab:green")
plt.title("Evolução do preço de fechamento das ações")
plt.xlabel("Dia")
plt.ylabel("Preço de fechamento (R$)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# a) Qual foi o maior preço registrado durante os 10 dias?

maior_preco = df["preco"].max()
print(df.loc[df["preco"] == maior_preco, ["dia", "preco"]])

# b) Qual foi o menor preço registrado?

menor_preco = df["preco"].min()
print(df.loc[df["preco"] == menor_preco, ["dia", "preco"]])

# c) Em quais dias ocorreram quedas no preço das ações?

# Compara o preço de cada dia com o do dia anterior.
df["variacao_preco"] = df["preco"].diff().round(2)
quedas = df.loc[df["variacao_preco"] < 0, ["dia", "preco", "variacao_preco"]]
print(quedas)

# d) Qual foi a média dos preços de fechamento?

preco_medio = df["preco"].mean()
print("Preço médio: R$", f"{preco_medio:.2f}".replace(".", ","))

# e) Se um investidor comprou 100 ações no primeiro dia e vendeu todas no último dia, qual seria o lucro obtido, desconsiderando taxas e impostos?

quantidade_acoes = 100
preco_compra = df["preco"].iloc[0]
preco_venda = df["preco"].iloc[-1]
valor_compra = quantidade_acoes * preco_compra
valor_venda = quantidade_acoes * preco_venda
lucro = valor_venda - valor_compra
print(pd.DataFrame({
    "descricao": ["Compra de 100 ações no D1", "Venda de 100 ações no D10", "Lucro bruto"],
    "valor_rs": [valor_compra, valor_venda, lucro]
}))
