# Data Science e Big Data na Indústria

Repositório com os materiais e apresentações das aulas de **Data Science e Big Data na Indústria** (SENAI).

## Conteúdo do Repositório

- `Aula 01 - Data Science e Big Data na Indústria.pdf`
- `Aula 02 - Data Science e Big Data na Indústria.pdf`
- `Aula 03 - Data Science e Big Data na Indústria.pdf`
- `Aula 04 - Data Science e Big Data na Indústria.pdf`

---

## 🚀 Como Configurar o Ambiente após Clonar

Você pode configurar o ambiente facilmente usando o **npm** ou o **pip** nativo:

### Opção 1: Via npm (Automatizado em 1 comando)
Após clonar o repositório, basta executar no terminal:
```bash
npm install
```
> O comando executará automaticamente o ciclo `postinstall`, instalando todas as bibliotecas Python necessárias (`pandas`, `numpy`, `matplotlib`, `scikit-learn`, `ipykernel`) e registrando o kernel **Python (Data Science)** no Jupyter.

Para testar se tudo está funcionando:
```bash
npm run test:env
```

### Opção 2: Via Python / pip (Padrão do ecossistema Python)
Caso prefira o fluxo nativo do Python:
```bash
pip install -r requirements.txt
python -m ipykernel install --user --name=datascience --display-name "Python (Data Science)"
```

---

## 💻 Extensões Recomendadas no VS Code
Ao abrir este repositório no VS Code, o editor sugerirá automaticamente a instalação das extensões necessárias (configuradas em `.vscode/extensions.json`):
- **Python** (`ms-python.python`)
- **Pylance** (`ms-python.vscode-pylance`)
- **Jupyter** (`ms-toolsai.jupyter`)
- **Jupyter Notebook Renderers** (`ms-toolsai.jupyter-renderers`)
