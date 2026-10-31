# Organização do repositório

## Onde guardar cada tipo de arquivo

| Tipo | Local |
| :--- | :--- |
| PDFs originais das aulas | `PDFS AULAS/` |
| Notebooks de referência do professor | `Codigos do Professor/` |
| Exemplos e exercícios | Pasta da respectiva aula |
| Bases dos exemplos da Aula 02 | `Aula02/dados/` |
| Base do notebook completo da Aula 03 | `Aula03/consumo_energetico_alunos.csv` |
| Comprovante da Aula 05 | `Aula05/entregas/` |
| Projeto aplicado | `Projeto/`, com dados, resultados, documentação e entregas próprios |
| Orientações gerais | `doc/` |

## Alterações de 31/10/2026

1. O notebook completo da Aula 02 foi movido para `Aula02/`, ao lado da pasta `dados/`. Nenhuma célula foi alterada nessa organização.
2. Foram removidas oito cópias redundantes dos CSVs da Aula 02 e uma cópia idêntica do guia da aula.
3. Foi removida uma cópia redundante do CSV da Aula 03. O notebook de entrega utiliza a base incorporada.
4. Os PDFs repetidos em `Aula02/Docs/` e `Aula03/Docs/` foram removidos; os originais idênticos permanecem em `PDFS AULAS/`.
5. `Aula05DSBDparte1.ipynb` saiu de `PDFS AULAS/` e foi para `Codigos do Professor/`.
6. O comprovante da Aula 05 foi colocado em `Aula05/entregas/`.

Foram removidas 12 cópias idênticas, totalizando aproximadamente 9,08 MiB. Os arquivos originais necessários, as saídas dos notebooks e os ambientes Python foram preservados. A pasta temporária ignorada em `PDFS AULAS/tmp/` contém scripts e rascunhos próprios; ela não foi apagada nesta organização.

Ao abrir um notebook, use a pasta indicada no guia da respectiva aula como diretório de trabalho. Não mova os CSVs necessários sem ajustar os caminhos de leitura.
