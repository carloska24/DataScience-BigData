# Bases de dados — o que deve ser mantido

Os arquivos de dados encontrados fora dos ambientes e caches são CSVs, que o Excel também consegue abrir. Não foram encontrados arquivos `.xlsx`, `.xls` ou `.xlsm` de trabalho nessas pastas.

| Local | Arquivos | Por que manter |
| :--- | :--- | :--- |
| `Aula02/dados/` | `producao.csv`, `base_p52.csv`, `base_p54.csv`, `manutencao.csv` | Dados lidos pelos exemplos de produção, viagens, vendas e manutenção |
| `Aula03/` | `consumo_energetico_alunos.csv` | Entrada do notebook completo da Aula 03 |
| `Projeto/data/` | `dados_manutencao.csv` | Entrada original do projeto de manutenção industrial |
| `Projeto/resultados/` | `comparacao_validacao.csv`, `importancias_validacao.csv`, `perfis_clusters.csv`, `taxas_por_maquina.csv` | Resultados exportados que permitem consultar a análise sem executar tudo novamente |

## Duplicatas verificadas

A igualdade dos arquivos removidos foi confirmada pelo hash SHA256:

- Aula 02: cada uma das quatro bases tinha três cópias. Agora existe uma cópia por base em `Aula02/dados/`.
- Aula 03: a cópia em `Entrega Colab Aula03/` era idêntica à base da pasta principal. O notebook de entrega lê dados incorporados no próprio arquivo, portanto essa segunda cópia foi removida.
- A base `Projeto/data/dados_manutencao.csv` é idêntica à base de manutenção da Aula 02. Foi mantida nos dois contextos para permitir que o projeto funcione de forma independente.

Os CSVs encontrados dentro de ambientes Python e caches pertencem às bibliotecas instaladas. Não são bases acadêmicas e não foram removidos individualmente.

Os dados de entrada e os resultados exportados foram preservados sem alterar seus valores.
