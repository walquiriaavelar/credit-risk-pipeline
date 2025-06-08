# Pipeline de Risco de Crédito

Este projeto simula um pipeline simples para classificação de risco de crédito de clientes, com base em dados fictícios de operações financeiras e score de bureau.

## Tecnologias

- Python (pandas)
- SQLite
- CSV

## Fluxo

1. Leitura dos dados brutos;
2. Classificação do risco com base em atraso e score;
3. Exportação para CSV e banco de dados SQLite.

## Como executar

```bash
pip install -r requirements.txt
python src/transform.py