## Conclusão e recomendações
A análise dos dados da S&M Industry Tech identificou 903 registros com falha em
uma base de 5.000 registros após a retirada das duplicatas, correspondendo a 18,06%.
A máquina M04 apresentou a maior taxa de falha, com 18,90%. A diferença em relação
às demais máquinas foi pequena, por isso esse resultado precisa ser considerado
junto com as condições de operação e o histórico de manutenção.

As horas de operação e a vibração apresentaram as relações mais evidentes com as
falhas. As horas de operação também tiveram a maior importância por permutação na
Random Forest. Os registros com falha apresentaram médias maiores de temperatura,
vibração, corrente elétrica e horas de operação. A pressão apresentou pouca
correlação linear com a ocorrência de falhas.

A Random Forest foi escolhida pelo maior F1 na validação. No teste, obteve acurácia
de 82,50%, precisão de 58,44%, recall de 23,94% e F1-score de 0,340. Apesar da acurácia,
o modelo identificou apenas 45 dos 188 registros com falha. Foram 143 falsos negativos
e 32 falsos positivos. Portanto, a capacidade de identificar falhas ainda foi baixa,
o que limita seu uso para apoiar decisões de manutenção.

O K-Means identificou três perfis operacionais. O grupo com maiores médias de horas
de operação e vibração apresentou a maior taxa de falha, de 31,95%. Outro grupo foi
formado por poucos registros com temperaturas muito elevadas, mostrando a necessidade
de conferir os valores extremos antes de interpretar esse perfil como uma condição normal de operação.

Com base nesses resultados, as principais ações propostas para a equipe de manutenção são:
- Acompanhar em conjunto as horas de operação, a vibração, a temperatura e a corrente elétrica.
- Verificar sensores com valores ausentes e medições extremas, especialmente de temperatura.
- Investigar o histórico da máquina M04 e as condições associadas aos registros com falha.
- Registrar as intervenções e as causas confirmadas das falhas para melhorar a qualidade da base.
- Ampliar o período de coleta e avaliar melhorias nos modelos com dados posteriores,
  considerando tanto as falhas não identificadas quanto os alarmes indevidos.

O estudo ficou limitado a cinco máquinas e a um período de aproximadamente seis
semanas. Os limites de operação dos equipamentos não foram fornecidos, dificultando
a avaliação dos outliers. Além disso, o rótulo informa a falha no próprio registro;
a previsão com antecedência exigiria definir um intervalo futuro e reorganizar
o treinamento para esse objetivo. O processamento com Spark foi local, sem avaliação
em um cluster com várias máquinas.
