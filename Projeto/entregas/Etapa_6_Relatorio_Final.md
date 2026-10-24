# Relatório final e recomendações de manutenção

### Projeto de Data Science e Big Data

| Identificação | Dados |
| :--- | :--- |
| **Aluno** | Carlos Alexandre Duarte Pereira |
| **Curso** | Data Science & Big Data Aplicados na Indústria |
| **Disciplina** | Data Science e Big Data |
| **Professor** | Me. Daniel Vieira |
| **Semestre** | 1º Semestre 2026 |
| **Data** | 24/10/2026 |

---

## 6. Entregáveis do projeto e recomendações finais

### 6.1 Objetivo do estudo

A S&M Industry Tech enfrenta paradas não planejadas de equipamentos. O estudo utilizou o histórico de operação das máquinas para investigar as condições associadas às falhas e avaliar como os dados podem apoiar a equipe de manutenção.

O trabalho reúne exploração e preparação dos dados, classificação com Machine Learning, agrupamento com K-Means e operações com PySpark. Este relatório consolida os resultados dessas etapas e apresenta recomendações baseadas nas evidências encontradas.

A análise considera a ocorrência de falha no próprio registro. A base utilizada não define um intervalo de antecedência para previsão. Portanto, os resultados representam a classificação das condições registradas e não uma demonstração de que a falha pode ser prevista horas antes de acontecer.

### 6.2 Base de dados e preparação

O arquivo original contém 5.050 registros e 8 atributos. As colunas são data e hora, identificação da máquina, temperatura, vibração, pressão, corrente elétrica, horas de operação e ocorrência de falha. O período observado vai de 1º de janeiro a 11 de fevereiro de 2026 e abrange cinco máquinas, identificadas de M01 a M05.

| Verificação | Resultado | Tratamento adotado |
| :--- | :--- | :--- |
| Duplicatas exatas | 50 registros | Remoção das linhas repetidas |
| Tamanho após a limpeza | 5.000 registros | Base utilizada nas análises seguintes |
| Valores ausentes após retirar duplicatas | 50 em cada uma das cinco variáveis operacionais | Mediana aprendida no treinamento dos classificadores |
| Datas | Sem valores inválidos após a conversão | Conversão para data e hora e ordenação temporal |
| Valores extremos | Temperatura máxima de 278,84 °C e vibração máxima de 15,12 mm/s | Sinalização para investigação, sem exclusão automática |

A retirada de duplicatas evita a contagem repetida de uma mesma observação. O preenchimento pela mediana mantém os registros com ausências e reduz a influência dos extremos em comparação com a média. Nos classificadores, o cálculo da mediana foi feito dentro do Pipeline, utilizando apenas os dados disponíveis para treinamento em cada ajuste.

Os outliers foram mantidos porque os limites técnicos dos equipamentos não constam na base. Uma medição elevada pode indicar uma situação de operação relevante ou um problema no sensor. Excluir esses valores sem investigação poderia retirar informações importantes sobre as falhas.

### 6.3 Principais descobertas

#### Frequência de falhas e comparação entre máquinas

Após a limpeza, 903 registros apresentaram falha, equivalentes a **18,06%** da base. Os outros 4.097 registros, ou **81,94%**, não apresentaram falha. Esse desequilíbrio exige cuidado com a acurácia: acertar a classe mais frequente pode gerar um percentual alto de acertos sem identificar as falhas.

| Máquina | Registros | Registros com falha | Taxa de falha |
| :--- | ---: | ---: | ---: |
| M01 | 1.000 | 175 | 17,50% |
| M02 | 1.000 | 178 | 17,80% |
| M03 | 1.000 | 181 | 18,10% |
| M04 | 1.000 | 189 | 18,90% |
| M05 | 1.000 | 180 | 18,00% |

A M04 apresentou a maior taxa observada. A diferença para a M01, que teve a menor taxa, foi de 1,40 ponto percentual. Esse resultado justifica uma investigação do histórico da M04, mas não comprova que a máquina seja menos confiável. As condições de uso e as intervenções realizadas também precisam ser consideradas.

#### Condições operacionais associadas às falhas

| Variável | Média sem falha | Média com falha | Correlação com falha |
| :--- | ---: | ---: | ---: |
| Temperatura (°C) | 66,46 | 70,11 | 0,112 |
| Vibração (mm/s) | 2,93 | 3,64 | 0,304 |
| Pressão (bar) | 6,51 | 6,47 | -0,022 |
| Corrente elétrica (A) | 25,46 | 26,61 | 0,163 |
| Horas de operação | 5.483,84 | 8.887,35 | 0,381 |

As horas de operação e a vibração apresentaram as maiores correlações lineares com a falha. As médias dessas variáveis também foram maiores nos registros com falha. Temperatura e corrente elétrica apresentaram associação positiva mais fraca. A pressão teve pouca correlação linear com o alvo.

Esses resultados indicam que o acompanhamento conjunto das medições pode ser mais útil que a observação isolada de um sensor. A correlação, entretanto, não demonstra causa e efeito e não fornece, sozinha, um limite seguro para emitir alertas.

### 6.4 Modelo de classificação escolhido

Os atributos utilizados foram temperatura, vibração, pressão, corrente elétrica e horas de operação. O alvo foi a coluna `falha`. A identificação da máquina ficou fora do treinamento para concentrar a análise nas medições operacionais. A data serviu para organizar a divisão dos dados.

A separação respeitou a ordem temporal, com 3.000 registros para treino, 1.000 para validação e 1.000 para teste. Os modelos aprenderam com o período inicial e a avaliação final utilizou o período mais recente. Registros do mesmo instante permaneceram no mesmo conjunto.

Foram comparados Árvore de Decisão, Random Forest e Regressão Logística. Um classificador que sempre escolhe a classe mais frequente serviu de referência. O critério de escolha foi o F1-score da classe falha na validação, com recall como desempate.

| Modelo | Acurácia na validação | Precisão | Recall | F1-score |
| :--- | ---: | ---: | ---: | ---: |
| Random Forest | 84,70% | 58,46% | 23,17% | **0,332** |
| Regressão Logística | 84,80% | 60,34% | 21,34% | 0,315 |
| Árvore de Decisão | 84,80% | 71,43% | 12,20% | 0,208 |
| Referência: classe mais frequente | 83,60% | 0,00% | 0,00% | 0,000 |

A **Random Forest** apresentou o maior F1 na validação. Após essa escolha, o modelo foi treinado novamente com treino e validação reunidos. O teste permaneceu separado até a avaliação final.

| Métrica no teste | Resultado | Interpretação |
| :--- | ---: | :--- |
| Acurácia | 82,50% | 825 classificações corretas entre 1.000 registros |
| Precisão | 58,44% | 45 falhas confirmadas entre 77 registros classificados como falha |
| Recall | 23,94% | 45 falhas identificadas entre 188 existentes |
| F1-score | 0,340 | Equilíbrio ainda limitado entre precisão e recall |

As horas de operação tiveram a maior importância por permutação na validação para a Random Forest, seguidas pela vibração. Essa importância representa a redução do F1 ao embaralhar os valores de uma variável, mantendo as demais condições da avaliação.

### 6.5 Erros do modelo e consequências para a manutenção

| Situação observada | Previsão: sem falha | Previsão: com falha | Total |
| :--- | ---: | ---: | ---: |
| Sem falha | 780 | 32 | 812 |
| Com falha | 143 | 45 | 188 |
| Total | 923 | 77 | 1.000 |

Os **32 falsos positivos** representam registros sem falha que receberam classificação de falha. Em uma aplicação de manutenção, esse tipo de erro poderia gerar inspeções ou paradas desnecessárias.

Os **143 falsos negativos** representam falhas que o modelo não identificou. Isso corresponde a **76,06% das falhas do teste**. Esse foi o principal problema encontrado na classificação, pois limita a capacidade de detectar situações que exigem atenção.

Uma classificação constante de “sem falha” teria acurácia de 81,20% nesse mesmo teste. A acurácia de 82,50% da Random Forest ficou apenas 1,30 ponto percentual acima dessa referência. Por isso, a escolha do melhor modelo entre os candidatos não significa que o desempenho já seja suficiente para uso operacional.

O modelo precisa melhorar e passar por novas avaliações antes de funcionar como único critério de alerta. A base não informa os custos dos erros, portanto não permite calcular economia, prejuízo evitado ou retorno financeiro.

### 6.6 Perfis identificados pelo K-Means

O K-Means utilizou as cinco variáveis operacionais, com preenchimento dos ausentes e padronização. O alvo `falha` não participou do ajuste. As taxas de falha foram calculadas somente depois da formação dos grupos.

Foram comparadas quantidades de 2 a 6 clusters. A melhor silhueta entre os candidatos ocorreu com três grupos, com valor aproximado de 0,224. Esse resultado indica que ainda existe sobreposição entre os perfis.

| Cluster | Registros | Taxa de falha | Características observadas |
| :--- | ---: | ---: | :--- |
| 0 | 2.509 | 4,46% | Menores médias de horas de operação e vibração |
| 1 | 2.466 | 31,95% | Maiores médias de horas de operação e vibração |
| 2 | 25 | 12,00% | Temperatura média de 208,28 °C |

O cluster 1 concentrou uma proporção maior de falhas e pode orientar a investigação de condições de operação que merecem acompanhamento. Isso não significa que todo registro desse perfil apresente falha.

O cluster 2 mostrou como os extremos de temperatura influenciaram o agrupamento. Antes de tratar esse grupo como um perfil de operação, é necessário conferir os sensores e a consistência dessas medições. Os números dos clusters são apenas identificadores e não representam uma escala de gravidade.

### 6.7 Contribuição do PySpark

O PySpark realizou leitura do CSV, inspeção do schema, remoção de duplicatas, seleção de colunas, filtro dos registros com falha e agrupamentos por máquina, classe e dia. As contagens e taxas por máquina coincidiram com os resultados do Pandas.

A execução utilizou modo local. Como a base possui cerca de 5 mil registros, o Pandas foi suficiente para as análises realizadas. O trabalho não mediu desempenho em um cluster e não demonstrou ganho de velocidade com processamento distribuído.

Em uma coleta com mais equipamentos, sensores e registros frequentes, o Spark poderia dividir as tarefas de leitura, limpeza e agregação entre várias máquinas. Essa possibilidade depende da infraestrutura disponível e do volume de dados.

### 6.8 Recomendações técnicas

As ações abaixo são propostas baseadas na análise. Não representam intervenções já realizadas nem resultados operacionais comprovados.

| Prioridade proposta | Evidência | Ação recomendada | Forma de acompanhamento |
| :--- | :--- | :--- | :--- |
| Inicial | Ausências nas cinco variáveis operacionais | Verificar falhas de coleta e registrar a origem das ausências | Percentual de ausências por sensor e por máquina |
| Inicial | Temperaturas extremas e cluster com apenas 25 registros | Conferir calibração, unidade de medida e histórico das medições | Quantidade de extremos confirmados e corrigidos |
| Inicial | Maiores associações de horas de operação e vibração com falha | Acompanhar essas variáveis junto com temperatura e corrente | Evolução das medições e falhas confirmadas em cada condição |
| Inicial | M04 com taxa de 18,90% | Examinar histórico de uso, intervenções e condições de operação da M04 | Taxas por equipamento em períodos comparáveis |
| Desenvolvimento | Recall de 23,94% no teste | Avaliar ajustes de pesos das classes, parâmetros e limite de decisão usando dados de desenvolvimento | Recall, precisão, F1 e volume de alertas em nova avaliação |
| Desenvolvimento | Poucas informações sobre as intervenções | Registrar manutenção realizada, causa confirmada e componente afetado | Completude dos registros e confirmação dos rótulos de falha |
| Validação futura | Base de cinco máquinas e período curto | Ampliar a coleta e reservar novos períodos para teste | Desempenho por período e por equipamento |

Os ajustes propostos para o classificador são possibilidades para uma próxima análise, não melhorias já testadas neste trabalho. O teste atual não deve orientar novas escolhas de parâmetros. Após novos ajustes, será necessário avaliar o desempenho em dados ainda não utilizados.

Não foi definido um limite fixo de temperatura ou vibração para parada de máquina. Esse limite depende das especificações do fabricante, das condições de operação e da avaliação da equipe técnica.

### 6.9 Limitações

- O histórico abrange cinco máquinas e aproximadamente seis semanas, o que limita as conclusões sobre outros períodos ou equipamentos.
- A base não apresenta os limites técnicos de operação, as causas confirmadas das falhas nem os detalhes das intervenções.
- A manutenção dos outliers evita descartar sinais relevantes, mas pode influenciar as correlações e os agrupamentos.
- O recall baixo indica que grande parte das falhas passou sem identificação.
- As relações encontradas são associações e não comprovam causas físicas das falhas.
- O alvo descreve a falha no registro atual. Prever com antecedência exige definir um horizonte futuro e utilizar apenas informações anteriores a ele.
- O Spark foi utilizado localmente, sem comparação de desempenho distribuído.

### 6.10 Conclusão

O projeto mostrou que os dados operacionais podem ajudar a compreender as condições associadas às falhas. Horas de operação e vibração se destacaram tanto na análise exploratória quanto na importância dos atributos da Random Forest. Os agrupamentos também indicaram diferenças entre perfis com menores e maiores taxas de falha.

A Random Forest obteve o melhor F1 entre os classificadores comparados na validação, mas o resultado do teste evidenciou uma limitação importante: apenas 45 das 188 falhas foram identificadas. Dessa forma, as descobertas descritivas já oferecem pontos de investigação para a manutenção, enquanto a classificação ainda precisa de desenvolvimento e nova validação.

As prioridades propostas são melhorar a qualidade da coleta, verificar medições extremas, acompanhar os sensores em conjunto e registrar melhor as intervenções. Essas ações podem fornecer uma base mais consistente para estudos futuros e para a avaliação de ferramentas de apoio à manutenção.

### Referências

- Projeto Pós Data Science e BigData, Prof. Me. Daniel Vieira.
- Aula_03_DSBD.ipynb, material da disciplina.
- [Base de dados de manutenção disponibilizada no enunciado](https://drive.google.com/file/d/1yQ7P-mbRK3Gsh12ey6ahxk8szc6pOie1/view).
- Resultados das cinco etapas do notebook Projeto_Manutencao_Industrial.ipynb.
