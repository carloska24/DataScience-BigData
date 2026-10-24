# Projeto — Manutenção industrial

Trabalho de Data Science e Big Data da S&M Industry Tech, organizado a partir do
enunciado do Prof. Me. Daniel Vieira e do exemplo `Aula_03_DSBD.ipynb`.

## Arquivo principal

Abra **Projeto_Manutencao_Industrial.ipynb** no Google Colab e execute as células em ordem.
O notebook contém as cinco etapas, explicações, gráficos, modelos e conclusão.
Preencha aluno, curso, semestre e data na primeira célula.

O estilo segue a Aula 03: Pandas, inspeção com `head`, `info` e `describe`, gráficos,
tratamento de ausentes com `SimpleImputer`, modelos com `Pipeline`, métricas e árvore.
Não é necessário criar um site ou aplicativo para a entrega pedida.

## Estrutura

- `Projeto_Manutencao_Industrial.ipynb`: trabalho principal, com as análises.
- `data/dados_manutencao.csv`: base original baixada do link do enunciado, sem limpeza prévia.
- `resultados/`: tabelas e conclusão exportadas ao executar o notebook.
- `entregas/`: apresentação, relatório final em Markdown e notebook, e roteiro de apresentação.
- `doc/`: enunciado original do projeto em PDF.
- `entregas/GUIA_ESTUDO.md`: explicações para estudar e apresentar o trabalho.
- `requirements.txt`: bibliotecas para execução local.
- `criar_apresentacao.mjs`: script auxiliar para gerar a apresentação; requer as bibliotecas e ferramentas do ambiente Codex usadas na criação. Os arquivos temporários são gravados em `tmp/slides/`.

## Executar no Colab

1. Acesse https://colab.research.google.com/ e faça upload do notebook.
2. Execute a preparação do ambiente e depois as demais células na ordem.
3. A base é baixada automaticamente pelo link do professor. Como alternativa, envie
   o CSV da pasta `data` para a pasta de trabalho do Colab.
4. Confira as saídas, personalize a identificação e salve uma cópia do notebook executado.

## Executar localmente no Windows

Requer Python e Java 17 ou superior para o Spark 4.0.1. No ambiente deste projeto,
foi preparado um ambiente virtual na pasta `.venv`.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pip install jupyterlab
.venv/Scripts/python.exe -m ipykernel install --user --name manutencao-industrial --display-name "Python (Manutenção Industrial)"
.venv/Scripts/python.exe -m jupyter lab Projeto_Manutencao_Industrial.ipynb
```

Selecione o kernel **Python (Manutenção Industrial)** e execute as células em ordem.

## Escolhas metodológicas

- Remove apenas duplicatas exatas, verifica datas e sinaliza outliers sem descartá-los automaticamente.
- Mantém as ausências na exploração; imputa os atributos no Pipeline para os modelos.
- Usa divisão temporal de aproximadamente 60%/20%/20% (treino/validação/teste),
  mantendo o mesmo instante no mesmo conjunto.
- Escolhe o classificador pelo F1 na validação, com recall como desempate; usa o teste
  somente para avaliar o modelo escolhido após seu reajuste.
- Compara Árvore, Random Forest e Regressão Logística com um classificador de referência.
- Escolhe K-Means sem usar a classe de falha, comparando de 2 a 6 grupos.
- Executa operações reais de PySpark em modo local, sem afirmar ganho distribuído.

O objetivo é classificar o registro atual. Previsão com antecedência exigiria outro
alvo e outra avaliação. Os resultados não autorizam paradas automáticas de equipamentos.

## Fonte da base

Link fornecido no PDF:
https://drive.google.com/file/d/1yQ7P-mbRK3Gsh12ey6ahxk8szc6pOie1/view

O arquivo original tem 5.050 linhas e 8 colunas. Após remover 50 duplicatas exatas,
restam 5.000 registros. A impressão digital SHA256 do arquivo é exibida no notebook.

## Verificação realizada

Em 24/10/2026, as 24 células de código foram executadas integralmente, incluindo
as consultas de PySpark 4.0.1, com Java 21 no Windows. O notebook foi salvo com
as saídas e 13 gráficos. As contagens e as taxas por máquina calculadas com Pandas
e Spark coincidiram. A execução no serviço Google Colab não foi realizada nesta sessão.

A Random Forest teve o melhor F1 na validação. No teste final, atingiu acurácia
de 82,50%, precisão de 58,44%, recall de 23,94% e F1 de 0,340. A baixa detecção de
falhas está discutida na conclusão e é uma limitação importante do resultado.
