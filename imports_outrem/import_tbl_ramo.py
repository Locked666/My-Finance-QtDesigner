import sqlite3
import csv
import re

# Conectar ao banco de dados
conexao = sqlite3.connect(r'D:\Desenvolvimento\python\My-Finance-QtDesigner\database\database.db')
cursor = conexao.cursor()

# Ler o arquivo CSV com encoding alternativo (tente 'latin1' se 'utf-8' falhar)
with open(r'D:\Desenvolvimento\python\My-Finance-QtDesigner\imports_outrem\tbl_cod_ramo_ativ.csv', mode='r') as file:
    reader = csv.reader(file)
    for linha in reader:
        # Verificar se a linha contém elementos
        print(linha)
        if len(linha) > 0 and linha[0].strip():
            # Extrair código e descrição usando expressão regular
            match = re.match(r'(\d+(?:\.\d{2})?)\s*–\s*(.*)', linha[0])
            if match:
                codigo, descricao = match.groups()
                
                # Inserir no banco de dados
                cursor.execute('''
                INSERT INTO ramo_atividade (codigo, descricao) VALUES (?, ?)
                ''', (codigo, descricao))

# Salvar e fechar a conexão
conexao.commit()
conexao.close()

print("Dados inseridos com sucesso!")
