---

## ☁️ Integração com Databricks (estrutura futura)

O projeto foi estruturado para ser executado tanto localmente quanto no ambiente **Databricks**, com organização compatível com notebooks e agendamentos via **Databricks Workflows**.

### 🔹 Arquivo de Job

- `pipeline_job.json`: contém a definição do job agendado com:
  - Nome: `pipeline_operacoes_credito`
  - Task: `executar_credito`
  - Agendamento: diário às 07:00 (America/Sao_Paulo)

### 🔹 Notebook (versão Databricks)

- `notebooks/operacoes_credito.py`: estrutura de notebook que simula uma pipeline ETL com base no código do projeto.
- Adaptável para uso com tabelas Delta e leitura via Spark no Databricks.

### 🛠️ Próximos passos planejados

- Implementação da leitura e gravação de dados em **Delta Lake**
- Criação de tabelas no **Unity Catalog**
- Visualização de dados com **Databricks SQL**
- Deploy final com controle de versão por GitHub e agendamento via interface Databricks

---

> 🔍 Esse diferencial demonstra minha preparação técnica para atuar em ambientes reais de engenharia de dados em nuvem com ferramentas como o Databricks, conforme exigido na vaga da Ailos.
