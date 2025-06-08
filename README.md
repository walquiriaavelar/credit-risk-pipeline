# 💳 Pipeline de Risco de Crédito

Este projeto simula um pipeline de dados para **classificação de risco de crédito** de clientes, utilizando dados fictícios de operações financeiras e score de crédito.

O objetivo é demonstrar a aplicação de conceitos de **ETL (Extract, Transform, Load)** com Python e SQL, usando boas práticas de organização e automação de processos analíticos, conforme exigido em cenários como o da Ailos.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Pandas
- SQLite3
- CSV (dados brutos)
- Terminal (para execução e inspeção)

---

## 📊 Pipeline: Fluxo de Execução

1. **Extração:** leitura de arquivos `.csv` contendo dados de clientes e operações de crédito;
2. **Transformação:** classificação de risco baseada em regras de negócio (score de crédito e atraso de pagamento);
3. **Carga:** exportação dos dados classificados para:
   - Arquivo `.csv` final
   - Banco de dados relacional SQLite (`.db`)

---

## 📁 Estrutura do Projeto

credit-risk-pipeline/
├── data/
│ ├── clientes.csv
│ └── operacoes_credito.csv
├── src/
│ ├── transform.py
│ └── utils.py
├── output/
│ └── risco_credito_final.csv
├── database/
│ └── risco_credito.db
├── requirements.txt
└── README.md

# 1. Instale as dependências
pip install -r requirements.txt

# 2. Execute o pipeline
python -m src.transform

# Entrar no SQLite via terminal
sqlite3 database/risco_credito.db

# Listar tabelas
.tables

# Visualizar dados
SELECT * FROM tb_risco_credito LIMIT 10;
