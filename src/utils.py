def classificar_risco(row):
    if row['score_bureau'] >= 700 and row['atraso_dias'] == 0:
        return "Baixo"
    elif row['score_bureau'] >= 500 and row['atraso_dias'] <= 15:
        return "Médio"
    elif row['score_bureau'] < 500 and row['atraso_dias'] > 30:
        return "Alto"
    else:
        return "Crítico"