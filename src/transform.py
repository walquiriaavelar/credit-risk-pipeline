import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.utils import classificar_risco
import sqlite3

# Leitura dos dados
clientes = pd.read_csv("data/clientes.csv")
operacoes = pd.read_csv("data/operacoes_credito.csv")

# Merge
df = pd.merge(operacoes, clientes, on="id_cliente")

# Aplicar classificação de risco
df["classificacao_risco"] = df.apply(classificar_risco, axis=1)

# Exportar CSV
df.to_csv("output/risco_credito_final.csv", index=False)

# Exportar para SQLite
conn = sqlite3.connect("database/risco_credito.db")
df.to_sql("tb_risco_credito", conn, if_exists="replace", index=False)
conn.close()