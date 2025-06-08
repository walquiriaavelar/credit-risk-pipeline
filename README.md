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

bash
pip install -r requirements.txt
python src/transform.py
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Credit Risk Pipeline

## Objetivo
Pipeline de ingestão, transformação e análise de risco de crédito com agendamento automático no Databricks.

## Estrutura
- Leitura de dados Delta
- Criação de tabelas no Unity Catalog
- Criação de view de inadimplência
- Agendamento via Job (Databricks Workflows)

## View principal
`credit_risk.vw_operacoes_atraso`

## Job agendado
- Nome: `pipeline_operacoes_credito`
- Task: `executar_credito`
- Agendamento: Diário às 07:00 (America/Sao_Paulo)

## Execução
Importe o notebook, configure o job e execute manualmente ou aguarde a agenda.
