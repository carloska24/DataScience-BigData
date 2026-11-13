# Aula 06 — exercícios resolvidos

**Aluno:** Carlos Alexandre Duarte Pereira  
**Disciplina:** Python para Data Science  
**Professor:** Me. Daniel Vieira

Esta pasta acompanha a sequência das aulas do repositório. O [PDF original](Aula%2001%20-%20Python%20para%20Data%20Science.pdf) inicia a nova disciplina e está identificado como **Aula 01 — Python para Data Science**.

As resoluções seguem o padrão das aulas anteriores: identificação, dados do enunciado, código dividido em etapas, gráficos, respostas comentadas e conclusão. Os dados estão incorporados aos arquivos, sem necessidade de baixar CSVs.

| Exercício | Notebook com respostas e saídas | Programa Python | Páginas do PDF |
| :--- | :--- | :--- | :--- |
| 1 — Temperatura de uma máquina | [Exercicio01_Aula06.ipynb](Exercicio01_Aula06.ipynb) | [Exercicio01.py](Aula01-Ex1/Exercicio01.py) | 37–39 |
| 2 — Vendas por setor e cliente | [Exercicio02_Aula06.ipynb](Exercicio02_Aula06.ipynb) | [Exercicio02.py](Aula01-Ex2/Exercicio02.py) | 40–42 |
| 3 — Preços de fechamento de ações | [Exercicio03_Aula06.ipynb](Exercicio03_Aula06.ipynb) | [Exercicio03.py](Aula01-Ex3/Exercicio03.py) | 43–45 |

## Executar os notebooks

Abra o notebook no VS Code, Jupyter ou Google Colab e execute todas as células em ordem. No Colab, use **Ambiente de execução → Executar tudo**. Os notebooks incluem os resultados da execução local; a execução no serviço Colab não foi verificada.

## Preparar o ambiente local

No PowerShell, a partir da raiz do repositório:

```powershell
cd Aula06
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
```

No VS Code, selecione `Aula06/.venv/Scripts/python.exe` como ambiente dos notebooks. O ambiente da pasta atende aos três exercícios. O nome `Aula01-Ex1` mantém a pasta solicitada no PDF; os outros programas seguem a mesma convenção.

Para executar os programas pelo terminal, ainda dentro de `Aula06`:

```powershell
python Aula01-Ex1/Exercicio01.py
python Aula01-Ex2/Exercicio02.py
python Aula01-Ex3/Exercicio03.py
```

Cada programa exibe um gráfico e imprime os cálculos. Feche a janela do gráfico para continuar a execução das respostas. Se a ativação do ambiente estiver indisponível, use `.venv/Scripts/python.exe` no lugar de `python` nos comandos de instalação e execução.

Ao terminar, use `deactivate` para sair do ambiente virtual.

## Resultados conferidos

- **Temperatura:** máxima de 45 °C às 14:00, mínima de 25 °C e média de 35,6 °C. A maior elevação foi de 4 °C em dois intervalos: 09:00–10:00 e 12:00–13:00.
- **Vendas:** Indústria e Tecnologia empataram no maior faturamento, com R$ 12.000,00 cada. Comércio somou R$ 6.000,00; a empresa faturou R$ 30.000,00. A maior compra foi a do cliente C8, de R$ 5.000,00.
- **Ações:** máximo de R$ 31,00 no D10, mínimo de R$ 25,50 no D1, média de R$ 28,13 e quedas no D3, D6 e D9. A operação com 100 ações gerou lucro bruto de R$ 550,00 nos valores do exercício.
