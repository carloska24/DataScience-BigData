<div align="center">

<img src="assets/banner.jpg" alt="Data Science e Big Data na Indústria" width="100%">

# Data Science & Big Data

### Dados industriais • Machine Learning • Processamento com Spark

Um espaço de estudo e aplicação de ciência de dados à indústria: das primeiras análises em Python à avaliação de modelos e à comunicação dos resultados.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

**[Começar](#inicio-rapido) · [Explorar as pastas](#estrutura-do-repositorio) · [Projeto industrial](#projeto-de-manutencao-industrial) · [Resultados](#resultados-do-projeto) · [Executar](#ambiente-e-execucao)**

</div>

---

<a id="visao-geral"></a>
## 🧭 Visão geral

Este repositório reúne materiais da disciplina **Data Science e Big Data na Indústria**, exercícios, notebooks de aula e um projeto aplicado de análise de falhas em equipamentos industriais.

O conteúdo está organizado para acompanhar o percurso de aprendizagem: compreender a base, explorar os dados, preparar as variáveis, comparar modelos, realizar agregações com PySpark e apresentar conclusões sustentadas pelas métricas.

| 📚 Estudo | 🔬 Prática | 🏭 Aplicação |
| :--- | :--- | :--- |
| PDFs e exemplos do professor | Notebooks, exercícios e orientações de ambiente | Análise de manutenção industrial, relatório e apresentação |
| [Materiais das aulas](PDFS%20AULAS/) | [Aula 02](Aula02/) · [Aula 03](Aula03/) | [Abrir o projeto](Projeto/) |

<a id="inicio-rapido"></a>
## ⚡ Início rápido

Escolha o caminho conforme seu objetivo:

| Quero… | Onde começar |
| :--- | :--- |
| Conhecer o trabalho aplicado | [Notebook de manutenção industrial](Projeto/Projeto_Manutencao_Industrial.ipynb) |
| Ler as conclusões e recomendações | [Relatório final](Projeto/entregas/Etapa_6_Relatorio_Final.md) |
| Ver os slides | [Apresentação em PowerPoint](Projeto/entregas/Apresentacao_Manutencao_Industrial.pptx) |
| Estudar para apresentar | [Guia de estudo](Projeto/entregas/GUIA_ESTUDO.md) · [Roteiro](Projeto/entregas/Roteiro_Apresentacao.md) |
| Acompanhar os exercícios | [Aula 02](Aula02/) · [Aula 03](Aula03/) |
| Preparar o computador | [Ambiente e execução](#ambiente-e-execucao) |
| Consultar os enunciados | [PDFs das aulas](PDFS%20AULAS/) · [Enunciado do projeto](Projeto/doc/) |

É possível ler os notebooks com suas saídas diretamente no GitHub. Para executar ou alterar as análises, use Jupyter, VS Code ou Google Colab.

<a id="estrutura-do-repositorio"></a>
## 🗂️ Estrutura do repositório

```text
DataScience-BigData/
├── .vscode/                          # Extensões recomendadas para o editor
├── assets/                           # Imagens usadas na documentação
├── Aula02/
│   ├── Aula02_Completa_com_Dados/     # Exemplos completos da aula
│   ├── Docs/                         # Material de referência
│   └── Exercicios Aula02/            # Exercícios e comprovante de entrega
├── Aula03/
│   ├── Docs/                         # Material e instruções de execução
│   ├── Entrega Colab Aula03/         # Notebook de entrega e dados
│   ├── assets/                       # Imagens de apoio
│   ├── Aula03_Todos_os_Exemplos_Completo.ipynb
│   ├── consumo_energetico_alunos.csv
│   ├── package.json
│   └── requirements.txt
├── Codigos do Professor/             # Notebooks de referência do professor
├── PDFS AULAS/                       # PDFs das aulas 01 a 04
├── Projeto/
│   ├── data/                         # Base original de manutenção
│   ├── doc/                          # Enunciado original em PDF
│   ├── entregas/                     # Relatório, slides e materiais de apresentação
│   ├── resultados/                   # Tabelas, métricas e conclusão exportadas
│   ├── Projeto_Manutencao_Industrial.ipynb
│   ├── criar_apresentacao.mjs         # Fonte auxiliar da apresentação
│   ├── requirements.txt              # Dependências específicas do projeto
│   └── README.md                     # Documentação do trabalho aplicado
├── doc/                              # Guias de ambiente e notebooks introdutórios
├── .gitignore                        # Regras para arquivos locais e temporários
├── package.json                      # Atalhos opcionais de configuração
├── requirements.txt                  # Dependências gerais das aulas
└── README.md                         # Página inicial do repositório
```

A árvore destaca os diretórios e arquivos principais. Cada pasta de aula pode conter materiais complementares.

<a id="projeto-de-manutencao-industrial"></a>
## 🏭 Projeto de manutenção industrial

O estudo utiliza o contexto da **S&M Industry Tech**, com o objetivo de investigar condições associadas às falhas e avaliar modelos de classificação. O trabalho segue o enunciado do **Prof. Me. Daniel Vieira**.

| Aspecto | Descrição |
| :--- | :--- |
| Base original | 5.050 registros e 8 colunas |
| Base após deduplicação | 5.000 registros, após remover 50 duplicatas exatas |
| Equipamentos | Cinco máquinas |
| Variáveis operacionais | Temperatura, vibração, pressão, corrente elétrica e horas de operação |
| Alvo | Ocorrência de falha no registro atual |
| Classificação | Árvore de Decisão, Random Forest, Regressão Logística e referência majoritária |
| Agrupamento | K-Means, comparando de 2 a 6 grupos |
| Processamento | Pandas e PySpark em modo local |

### Percurso da análise

| Etapa | O que é feito | Entrega |
| :--- | :--- | :--- |
| 01 · Exploração | Inspeção, estatísticas, distribuições e relações entre variáveis | Tabelas e gráficos no notebook |
| 02 · Preparação | Verificação de datas, duplicatas, ausências e valores extremos | Base preparada e critérios documentados |
| 03 · Classificação | Separação temporal, pipelines, comparação e escolha do modelo | Métricas de validação e teste |
| 04 · Agrupamento | Imputação, padronização e avaliação de grupos | Perfis operacionais dos clusters |
| 05 · PySpark | Leitura, filtros, deduplicação e agregações | Conferência com os resultados do Pandas |
| 06 · Comunicação | Interpretação dos resultados e recomendações | Relatório final, apresentação e roteiro |

### Critérios metodológicos

- A separação dos dados respeita a ordem temporal: aproximadamente **60% para treino, 20% para validação e 20% para teste**. Registros do mesmo instante ficam no mesmo conjunto.
- A imputação dos atributos ocorre nos pipelines dos classificadores, com ajuste nos dados de treinamento.
- A seleção do classificador utiliza o **F1 da classe falha na validação**, com recall como desempate. O teste avalia o modelo escolhido após reajuste com treino e validação.
- Valores extremos são sinalizados e discutidos, sem exclusão automática.
- A coluna `falha` não participa do ajuste do K-Means; as taxas por grupo são analisadas depois.
- O uso de Spark demonstra operações de processamento em modo local. O estudo não apresenta medição de ganho de desempenho em um cluster distribuído.

<a id="resultados-do-projeto"></a>
## 📊 Resultados do projeto

A **Random Forest** apresentou o melhor F1 entre os classificadores comparados na validação. Na avaliação final, com 1.000 registros de teste, os resultados exportados foram:

| Acurácia | Precisão | Recall | F1-score |
| :---: | :---: | :---: | :---: |
| **82,50%** | **58,44%** | **23,94%** | **0,340** |

O modelo identificou **45 das 188 falhas** do teste. As 143 falhas não identificadas mostram que o recall ainda é limitado. Uma previsão constante de “sem falha” teria 81,20% de acurácia nesse conjunto; por isso, a acurácia isolada não descreve bem a capacidade de detectar falhas.

O alvo representa a condição do registro atual. A previsão de uma falha com antecedência exigiria outro alvo, um horizonte futuro e uma avaliação específica.

| Arquivo | Conteúdo |
| :--- | :--- |
| [comparacao_validacao.csv](Projeto/resultados/comparacao_validacao.csv) | Comparação dos modelos na validação |
| [metricas_teste.json](Projeto/resultados/metricas_teste.json) | Métricas finais do classificador escolhido |
| [importancias_validacao.csv](Projeto/resultados/importancias_validacao.csv) | Importância dos atributos na validação |
| [perfis_clusters.csv](Projeto/resultados/perfis_clusters.csv) | Resumo dos grupos encontrados |
| [taxas_por_maquina.csv](Projeto/resultados/taxas_por_maquina.csv) | Frequência de falhas por equipamento |
| [conclusao.md](Projeto/resultados/conclusao.md) | Interpretação e recomendações |

Os números acima documentam a execução salva no projeto. Consulte o [relatório final](Projeto/entregas/Etapa_6_Relatorio_Final.md) para os erros do modelo, os perfis de agrupamento e as limitações da análise.

<a id="ambiente-e-execucao"></a>
## 💻 Ambiente e execução

### 1. Obter o repositório

```powershell
git clone https://github.com/carloska24/DataScience-BigData.git
cd DataScience-BigData
```

### 2. Preparar o ambiente das aulas no Windows

Os comandos abaixo usam o executável do ambiente virtual diretamente, sem exigir ativação no PowerShell.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pip install jupyterlab
.venv/Scripts/python.exe -m ipykernel install --user --name datascience --display-name "Python (Data Science)"
.venv/Scripts/python.exe -m jupyter lab
```

No Jupyter ou no VS Code, selecione o kernel **Python (Data Science)**. Execute as células do notebook em ordem para manter os dados e as variáveis consistentes.

### 3. Preparar o projeto industrial

O projeto possui dependências próprias, incluindo **PySpark 4.0.1**, Seaborn, gdown e ferramentas de notebook. Para reproduzir o ambiente registrado na documentação, utilize **Java 17 ou superior**; a execução documentada utilizou Java 21 no Windows.

```powershell
cd Projeto
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pip install jupyterlab
.venv/Scripts/python.exe -m ipykernel install --user --name manutencao-industrial --display-name "Python (Manutenção Industrial)"
java -version
.venv/Scripts/python.exe -m jupyter lab Projeto_Manutencao_Industrial.ipynb
```

Selecione o kernel **Python (Manutenção Industrial)**. Mantenha a pasta `Projeto` como diretório de trabalho para que os caminhos relativos de `data/` e `resultados/` sejam resolvidos corretamente.

### 4. Executar no Google Colab

1. Envie [Projeto_Manutencao_Industrial.ipynb](Projeto/Projeto_Manutencao_Industrial.ipynb) ao Google Colab.
2. Confira a identificação do trabalho na primeira célula.
3. Execute a preparação do ambiente e as demais células em ordem.
4. O notebook prevê o download da base pelo link do enunciado. Se necessário, envie também o CSV de `Projeto/data/`, seguindo o caminho indicado no notebook.
5. Salve a versão executada e confira os resultados antes da entrega.

A documentação do projeto registra execução local; a execução no serviço Colab não foi verificada naquela sessão.

<details>
<summary><strong>Configuração opcional com npm</strong></summary>

O `package.json` da raiz oferece atalhos para instalar as dependências Python das aulas e registrar o kernel. Node.js e npm são necessários somente para esses atalhos.

```powershell
npm install
npm run test:env
```

O `postinstall` chama `python -m pip` e registra um kernel no usuário. Confira qual Python está selecionado antes de executar. Para abrir pelo comando `npm start`, instale também o pacote `notebook` no mesmo ambiente:

```powershell
python -m pip install notebook
npm start
```

As dependências específicas de `Projeto/requirements.txt` precisam ser instaladas separadamente para o trabalho industrial.

</details>

<details>
<summary><strong>Extensões recomendadas para VS Code</strong></summary>

O arquivo `.vscode/extensions.json` recomenda:

- **Python** — execução e seleção do interpretador.
- **Pylance** — suporte de linguagem e análise de código.
- **Jupyter** — edição e execução dos notebooks.
- **Jupyter Notebook Renderers** — renderização de saídas dos notebooks.

Consulte também o [guia de ambiente](doc/COMO_EXECUTAR.md) e as [orientações da Aula 03](Aula03/Docs/COMO_EXECUTAR.md).

</details>

## 🧰 Tecnologias e responsabilidades

| Tecnologia | Papel no repositório |
| :--- | :--- |
| Python | Preparação dos dados e implementação das análises |
| Pandas e NumPy | Manipulação de tabelas e operações numéricas |
| Matplotlib e Seaborn | Gráficos e análise exploratória |
| Scikit-learn | Pipelines, imputação, classificação, agrupamento e métricas |
| PySpark | Operações de leitura, transformação e agregação |
| Jupyter / VS Code / Colab | Leitura, edição e execução dos notebooks |
| Markdown e PowerPoint | Documentação e apresentação dos resultados |

## 📦 Entregas e reprodutibilidade

O [notebook principal](Projeto/Projeto_Manutencao_Industrial.ipynb) reúne as análises e saídas. A pasta [entregas](Projeto/entregas/) contém as versões voltadas à leitura e à apresentação do trabalho.

Para repetir a análise, mantenha a base original, instale as dependências da pasta correspondente, execute as células em sequência e confira as tabelas exportadas. A divisão temporal, a semente e os critérios de avaliação estão descritos no notebook. Os requisitos possuem faixas de versões; não constituem um congelamento completo do ambiente.

Ambientes virtuais, caches e arquivos temporários são ignorados pelo Git. Resultados, dados de estudo e entregas fazem parte do conteúdo versionado.

O script `Projeto/criar_apresentacao.mjs` preserva a fonte auxiliar dos slides e depende das bibliotecas e ferramentas do ambiente Codex usadas na criação. A apresentação `.pptx` já está disponível em `Projeto/entregas/` para leitura e edição.

## 👤 Autoria e referências

**Aluno:** Carlos Alexandre Duarte Pereira · [@carloska24](https://github.com/carloska24)

**Disciplina:** Data Science e Big Data na Indústria  
**Professor do projeto:** Prof. Me. Daniel Vieira

Os PDFs e códigos do professor são materiais de referência acadêmica e permanecem atribuídos aos respectivos autores. A base de manutenção foi disponibilizada no [link indicado no enunciado](https://drive.google.com/file/d/1yQ7P-mbRK3Gsh12ey6ahxk8szc6pOie1/view).

---

<div align="center">

**Explorar os dados · Avaliar as evidências · Comunicar os resultados**

[Voltar ao início](#data-science--big-data)

</div>
