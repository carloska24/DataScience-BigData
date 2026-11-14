# Aula 07 — Exercícios Resolvidos: Condicionais e Repetições

**Aluno:** Carlos Alexandre Duarte Pereira  
**Curso:** Data Science & Big Data Aplicados na Indústria  
**Disciplina:** Python para Data Science  
**Professor:** Me. Daniel Vieira  
**Data:** 14/11/2026  

Esta pasta reúne a resolução completa dos exercícios práticos apresentados no PDF oficial [Aula 02 - Python para Data Science.pdf](Aula%2002%20-%20Python%20para%20Data%20Science.pdf).

O material está organizado em **cadernos Jupyter (.ipynb)** individuais e consolidados, além de **programas autônomos (.py)** localizados na pasta `programas/`. Todos os arquivos já contêm as saídas da execução registradas.

---

## 🗂️ Estrutura dos Arquivos

```text
Aula07/
├── Aula 02 - Python para Data Science.pdf     # Material didático original
├── Exercicio01_Aula07.ipynb a Exercicio20_Aula07.ipynb # 20 cadernos individuais
├── Exercicios_Condicionais_Aula07.ipynb       # Caderno consolidado do Bloco 1 (Ex 01 a 15)
├── Exercicios_Repeticao_Aula07.ipynb          # Caderno consolidado do Bloco 2 (Ex 16 a 20)
├── requirements.txt                          # Dependências de execução
├── README.md                                 # Esta documentação
└── programas/                                # Scripts Python (.py) para execução em terminal
    ├── ex01_maior_numero.py
    ├── ex02_crescimento_producao.py
    ├── ex03_precos_carros.py
    ├── ex04_menor_preco.py
    ├── ex05_combustiveis.py
    ├── ex06_vendas_imoveis.py
    ├── ex07_calculadora.py
    ├── ex08_desconto_loja.py
    ├── ex09_consumo_maquinas.py
    ├── ex10_desempenho_vendedores.py
    ├── ex11_sensor_temperatura.py
    ├── ex12_temp_vibracao.py
    ├── ex13_login_senha.py
    ├── ex14_compra_vip.py
    ├── ex15_ambiente_industrial.py
    ├── ex16_while_1_a_100.py
    ├── ex17_tabuada_for.py
    ├── ex18_soma_10_numeros.py
    ├── ex19_media_notas.py
    └── ex20_temperatura_maquinas.py
```

---

## 📋 Inventário Completo de Exercícios

### Bloco 1: Estruturas Condicionais e Operadores Lógicos (Páginas 26 a 34)

| Nº | Título | Notebook Individual | Script Python | Pág. PDF | Tema Principal |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | Maior entre dois números | [Exercicio01_Aula07.ipynb](Exercicio01_Aula07.ipynb) | [ex01_maior_numero.py](programas/ex01_maior_numero.py) | 26 | Comparação `if/elif/else` |
| **02** | Crescimento da produção | [Exercicio02_Aula07.ipynb](Exercicio02_Aula07.ipynb) | [ex02_crescimento_producao.py](programas/ex02_crescimento_producao.py) | 26 | Avaliação de variação percentual |
| **03** | Preços médios de carros (3 anos) | [Exercicio03_Aula07.ipynb](Exercicio03_Aula07.ipynb) | [ex03_precos_carros.py](programas/ex03_precos_carros.py) | 26 | Máximo e mínimo em séries |
| **04** | Menor preço entre três produtos | [Exercicio04_Aula07.ipynb](Exercicio04_Aula07.ipynb) | [ex04_menor_preco.py](programas/ex04_menor_preco.py) | 26 | Tomada de decisão de compras |
| **05** | Desconto em combustíveis | [Exercicio05_Aula07.ipynb](Exercicio05_Aula07.ipynb) | [ex05_combustiveis.py](programas/ex05_combustiveis.py) | 27 | Condicionais aninhadas por tipo/litros |
| **06** | Vendas anuais de imóveis | [Exercicio06_Aula07.ipynb](Exercicio06_Aula07.ipynb) | [ex06_vendas_imoveis.py](programas/ex06_vendas_imoveis.py) | 28 | Diretrizes de gestão por faixas |
| **07** | Calculadora matemática | [Exercicio07_Aula07.ipynb](Exercicio07_Aula07.ipynb) | [ex07_calculadora.py](programas/ex07_calculadora.py) | 29 | Operadores e prevenção de divisão por zero |
| **08** | Descontos progressivos na loja | [Exercicio08_Aula07.ipynb](Exercicio08_Aula07.ipynb) | [ex08_desconto_loja.py](programas/ex08_desconto_loja.py) | 30 | Faixas progressivas de compras |
| **09** | Consumo energético de máquinas | [Exercicio09_Aula07.ipynb](Exercicio09_Aula07.ipynb) | [ex09_consumo_maquinas.py](programas/ex09_consumo_maquinas.py) | 31 | Potência x Horas (kWh) |
| **10** | Avaliação de meta de vendedores | [Exercicio10_Aula07.ipynb](Exercicio10_Aula07.ipynb) | [ex10_desempenho_vendedores.py](programas/ex10_desempenho_vendedores.py) | 32 | Metas e validação de dados |
| **11** | Sensor de temperatura de máquinas | [Exercicio11_Aula07.ipynb](Exercicio11_Aula07.ipynb) | [ex11_sensor_temperatura.py](programas/ex11_sensor_temperatura.py) | 33 | Faixas térmicas e alerta crítico |
| **12** | Monitoramento de Temp ou Vibração | [Exercicio12_Aula07.ipynb](Exercicio12_Aula07.ipynb) | [ex12_temp_vibracao.py](programas/ex12_temp_vibracao.py) | 34 | Operador lógico `or` |
| **13** | Autenticação de usuário e senha | [Exercicio13_Aula07.ipynb](Exercicio13_Aula07.ipynb) | [ex13_login_senha.py](programas/ex13_login_senha.py) | 34 | Operador lógico `and` |
| **14** | Desconto para compra ou cliente VIP | [Exercicio14_Aula07.ipynb](Exercicio14_Aula07.ipynb) | [ex14_compra_vip.py](programas/ex14_compra_vip.py) | 34 | Operador lógico `or` |
| **15** | Monitoramento de Temp e Umidade | [Exercicio15_Aula07.ipynb](Exercicio15_Aula07.ipynb) | [ex15_ambiente_industrial.py](programas/ex15_ambiente_industrial.py) | 34 | Operador lógico `and` |

Caderno consolidado do Bloco 1: **[Exercicios_Condicionais_Aula07.ipynb](Exercicios_Condicionais_Aula07.ipynb)**

---

### Bloco 2: Estruturas de Repetição (Página 42)

| Nº | Título | Notebook Individual | Script Python | Pág. PDF | Tema Principal |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **16** | Contagem de 1 a 100 | [Exercicio16_Aula07.ipynb](Exercicio16_Aula07.ipynb) | [ex16_while_1_a_100.py](programas/ex16_while_1_a_100.py) | 42 | Laço `while` e incremento |
| **17** | Tabuada de 1 a 10 | [Exercicio17_Aula07.ipynb](Exercicio17_Aula07.ipynb) | [ex17_tabuada_for.py](programas/ex17_tabuada_for.py) | 42 | Laço `for` com `range(1, 11)` |
| **18** | Soma de 10 números | [Exercicio18_Aula07.ipynb](Exercicio18_Aula07.ipynb) | [ex18_soma_10_numeros.py](programas/ex18_soma_10_numeros.py) | 42 | Acumulador e somatório |
| **19** | Média das notas de 5 alunos | [Exercicio19_Aula07.ipynb](Exercicio19_Aula07.ipynb) | [ex19_media_notas.py](programas/ex19_media_notas.py) | 42 | Coleta em loop e média |
| **20** | Inspeção térmica de 10 máquinas | [Exercicio20_Aula07.ipynb](Exercicio20_Aula07.ipynb) | [ex20_temperatura_maquinas.py](programas/ex20_temperatura_maquinas.py) | 42 | Contador de alertas e média térmica |

Caderno consolidado do Bloco 2: **[Exercicios_Repeticao_Aula07.ipynb](Exercicios_Repeticao_Aula07.ipynb)**

---

## 💻 Instruções de Execução

### No VS Code / Antigravity IDE:
1. Abra qualquer um dos cadernos `.ipynb`.
2. Certifique-se de que o interpretador Python selecionado no topo direito possui as bibliotecas básicas instaladas (`Python 3.13` ou seu ambiente virtual).
3. Clique em **Run All** para re-executar todas as células em ordem.

### No Terminal PowerShell:
Para executar qualquer exercício de forma autônoma pelo terminal:
```powershell
cd Aula07
python programas/ex01_maior_numero.py
python programas/ex05_combustiveis.py
python programas/ex20_temperatura_maquinas.py
```
