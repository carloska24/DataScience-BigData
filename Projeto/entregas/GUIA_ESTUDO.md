# Guia para entender e apresentar o trabalho

## 1. Comece pelo problema

A empresa quer entender em quais condições as máquinas falham. Cada linha é uma
observação de uma máquina; não é uma máquina inteira. A coluna `falha` informa a
classe dessa observação. Não sabemos quanto tempo antes de uma falha seria possível agir.

## 2. Conheça a base antes de treinar

`head()` mostra exemplos, `info()` mostra tipos e ausências, e `describe()` resume
as variáveis numéricas. Observe as diferenças entre contagem de falhas e taxa:
uma máquina com mais registros pode ter mais falhas, sem ter maior proporção de falhas.

Não copie apenas os números: procure explicar o que eles significam para a empresa.

## 3. Entenda a limpeza

Duplicatas exatas repetem a mesma observação. Ausência de temperatura não significa
temperatura zero. Por isso usamos a mediana, calculada no período de treino.
Um valor extremo pode ser erro ou evento real; sem uma regra técnica, sinalizamos
para investigação em vez de simplesmente apagá-lo.

O `Pipeline` reúne preparação e modelo. Ele evita que informações dos dados de
avaliação participem do cálculo da mediana usada no treinamento.

## 4. Compare os classificadores

- A Árvore de Decisão aprende perguntas sucessivas sobre os atributos.
- A Random Forest combina várias árvores.
- A Regressão Logística estima uma probabilidade para a classe, apesar do nome “regressão”.
- O classificador de referência sempre escolhe a classe majoritária. Ele mostra por
  que olhar somente a acurácia pode enganar.

O conjunto de validação ajuda a escolher o modelo. O teste é uma avaliação final,
com registros de um período posterior. Não altere o modelo para melhorar o resultado
do teste sem reservar novos dados para outra avaliação.

Na matriz de confusão, concentre-se nos falsos negativos (falhas que passaram) e
nos falsos positivos (alarmes indevidos). Um bom trabalho explica ambos os erros.

## 5. Separe o objetivo do K-Means

O K-Means procura grupos parecidos, sem receber a resposta `falha`. Depois de formar
os grupos, verificamos se há diferenças nas taxas de falha. O identificador do grupo
não indica gravidade: o cluster 2 não é automaticamente pior que o cluster 1.

## 6. Explique por que usar Spark aqui

A base pequena pode ser analisada com Pandas. O uso de Spark atende à etapa prática
do projeto e mostra como escrever operações que também podem ser utilizadas em uma
infraestrutura distribuída. Rodar localmente não comprova vantagem de desempenho.

## Relação com a Aula 03

O projeto preserva a sequência de exploração, limpeza, visualização, `Pipeline`,
treinamento, métricas e visualização de árvore. Foram adicionados os conteúdos
solicitados no enunciado: Regressão Logística, K-Means e PySpark.
Foi usada separação temporal para manter observações posteriores fora do treino.
Não foi necessário codificar categorias porque os atributos escolhidos são numéricos.

Antes de entregar, preencha sua identificação e execute o notebook. Tente explicar
cada gráfico com suas palavras; as células de interpretação servem de apoio.
