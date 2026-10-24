# Roteiro de apresentação

**Aluno:** Carlos Alexandre Duarte Pereira  
**Disciplina:** Data Science e Big Data  
**Duração sugerida:** 10 a 12 minutos

## Slide 1 — Análise de falhas em equipamentos industriais

Este trabalho analisa as condições de operação de cinco máquinas da S&M Industry Tech. O objetivo foi entender quais variáveis aparecem associadas às falhas e comparar modelos de classificação. A apresentação resume o caminho da preparação dos dados até as recomendações de manutenção. O foco é explicar os resultados encontrados, inclusive as limitações do classificador.

## Slide 2 — Problema e objetivo

A empresa enfrenta paradas não planejadas e utiliza parte da manutenção de forma corretiva. A proposta foi investigar os dados que já existem para apoiar a compreensão das falhas. Cada linha representa uma observação de uma máquina. O alvo vale zero quando não existe falha registrada e um quando existe. Esse detalhe é importante porque o trabalho classifica a condição do registro. Para prever com antecedência, seria necessário definir, por exemplo, se a máquina falhará nas próximas horas e reorganizar a base.

## Slide 3 — Base de dados e qualidade

O arquivo original possui 5.050 linhas e oito colunas. Foram retiradas 50 duplicatas exatas, restando cinco mil registros. Depois dessa limpeza, cada sensor apresentou 50 valores ausentes. Nos classificadores, a mediana foi calculada apenas com os dados de treinamento, dentro do Pipeline. Os valores extremos foram mantidos porque a base não informa os limites físicos de operação. Uma temperatura de 278,84 graus exige investigação, mas a estatística sozinha não permite afirmar se é um defeito do sensor ou uma condição real.

## Slide 4 — Variáveis associadas às falhas

O gráfico mostra a correlação de Pearson entre as medições e a coluna falha. Horas de operação teve o maior valor, aproximadamente 0,381, seguida por vibração, com 0,304. Temperatura e corrente também apresentaram associação positiva, porém mais fraca. A pressão ficou próxima de zero. As médias de horas e vibração foram maiores entre os registros com falha. Esses resultados apoiam o acompanhamento conjunto dos sensores, mas não provam que uma variável cause a falha nem permitem definir um limite automático de parada.

## Slide 5 — Treinamento e avaliação

A separação respeitou a ordem do tempo. Os três mil registros iniciais serviram para treino, os mil seguintes para validação e os mil finais para teste. A validação serviu para comparar Árvore de Decisão, Random Forest e Regressão Logística. O critério foi o F1 da classe falha porque ele combina precisão e recall. Depois da escolha, a Random Forest foi ajustada com treino e validação reunidos. O teste ficou reservado para a avaliação final. Essa separação evita escolher o modelo olhando diretamente o resultado que deve representar uma avaliação independente.

## Slide 6 — Comparação dos classificadores

A Random Forest apresentou o maior F1 na validação, aproximadamente 0,332. A Regressão Logística ficou em 0,315 e a Árvore de Decisão em 0,208. O modelo de referência escolhe sempre a classe sem falha e tem F1 igual a zero para a classe falha. A acurácia da árvore e da regressão foi ligeiramente maior, mas elas não foram escolhidas porque o critério definido era o F1. Esse resultado mostra por que a comparação depende da métrica adequada ao objetivo do problema.

## Slide 7 — Random Forest no teste

Depois do reajuste com treino e validação, a Random Forest atingiu acurácia de 82,50 por cento e precisão de 58,44 por cento no teste. O recall foi de apenas 23,94 por cento. Em termos simples, ela encontrou 45 das 188 falhas existentes. O F1 ficou em 0,340. A leitura principal é que a acurácia parece alta, mas o modelo deixa a maior parte das falhas passar. Por isso, o resultado ainda não sustenta usar esse classificador como único critério de alerta de manutenção.

## Slide 8 — Erros e impacto na manutenção

Nesta tabela, as linhas representam a situação registrada e as colunas representam a previsão. O modelo acertou 780 registros sem falha e 45 com falha. Os 32 falsos positivos poderiam gerar inspeções desnecessárias. O problema principal está nos 143 falsos negativos: eram falhas, mas o modelo respondeu sem falha. Isso equivale a 76,06 por cento das falhas do teste. A classe majoritária sozinha teria 81,20 por cento de acurácia nesse conjunto. Assim, o ganho de acurácia do modelo foi pequeno. Não foram calculados custos porque a base não fornece esses valores.

## Slide 9 — Perfis operacionais com K-Means

O K-Means agrupou os dados sem receber a coluna falha. Foram comparadas quantidades de dois a seis grupos e a melhor silhueta ocorreu com três. O cluster zero apresentou menores médias de horas de operação e vibração e taxa de falha de 4,46 por cento. No cluster um, essas médias foram maiores e a taxa chegou a 31,95 por cento. O cluster dois reúne apenas 25 registros, com temperatura média de 208,28 graus. Esse grupo evidencia a influência dos extremos e precisa ser investigado. A silhueta de 0,224 indica sobreposição, então esses perfis não são categorias definitivas de risco.

## Slide 10 — Processamento com PySpark

A etapa de PySpark repetiu operações de leitura, seleção, filtro e agrupamento. Foi possível contar registros, verificar ausências e calcular taxas de falha por máquina. As contagens e taxas coincidiram com o Pandas. O Spark rodou em modo local, com os recursos de uma máquina. Como a base tem cinco mil registros, o Pandas já era suficiente. A contribuição dessa etapa foi utilizar uma API que pode trabalhar de forma distribuída quando existe uma infraestrutura adequada e um volume maior de dados. O trabalho não mediu ganho de velocidade.

## Slide 11 — Recomendações para a manutenção

As primeiras recomendações estão ligadas à qualidade da coleta. Os sensores com ausências e as temperaturas extremas precisam ser verificados. Outra ação é acompanhar horas de operação e vibração junto com as outras medições, pois esses atributos apareceram associados às falhas. A M04 merece investigação do histórico, mas sua taxa não autoriza concluir que seja a pior máquina. Para o modelo, ajustes de pesos das classes e do limite de decisão são possibilidades futuras, ainda não testadas. Esses ajustes precisam usar os dados de desenvolvimento e depois passar por avaliação em um novo período. Também é importante registrar as causas das falhas e as intervenções.

## Slide 12 — Conclusões e limitações

O estudo encontrou associações úteis para orientar a investigação das falhas, principalmente envolvendo horas de operação e vibração. A classificação apresentou uma limitação clara: o modelo escolhido encontrou menos de um quarto das falhas no teste. Os agrupamentos ajudaram a descrever perfis, mas a sobreposição e os extremos exigem cuidado. O histórico contém cinco máquinas e aproximadamente seis semanas, sem limites técnicos completos dos equipamentos. O próximo passo é melhorar a qualidade da base e ampliar a avaliação com períodos novos. Para manutenção preditiva com antecedência, seria necessário definir outro alvo. A principal contribuição do trabalho foi transformar os registros em evidências para apoiar a análise da manutenção e mostrar os limites do que os modelos conseguiram identificar.

## Perguntas para discussão

### Por que a acurácia alta não foi suficiente?

A classe sem falha é majoritária. No teste, responder sempre sem falha já teria 81,20% de acurácia. O recall mostrou que o modelo encontrou somente 45 das 188 falhas.

### Por que não remover todos os outliers?

Valores extremos podem ser sinais reais de falha. Sem os limites técnicos do equipamento, a exclusão automática poderia retirar informação importante.

### Por que três clusters?

Entre as alternativas de dois a seis grupos, três apresentou a melhor silhueta. O valor de 0,224 e o grupo de temperatura extrema mostram que ainda é preciso cuidado na interpretação.

### O que poderia melhorar o classificador?

Ampliar os dados e avaliar pesos das classes, parâmetros e limite de decisão no conjunto de desenvolvimento. São propostas que exigem novo teste, sem reutilizar o teste atual para escolher ajustes.

### O modelo prevê uma falha antes de acontecer?

A avaliação considera o rótulo no próprio registro. A previsão antecipada exigiria definir um horizonte futuro e utilizar somente informações anteriores a ele.

### Por que usar Spark em uma base pequena?

Para aplicar as operações de processamento solicitadas no projeto. O Pandas foi suficiente para este volume, e o trabalho não comprovou ganho de desempenho com Spark.
