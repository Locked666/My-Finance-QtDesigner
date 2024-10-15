import sqlite3
import csv
import re

# Conectar ao banco de dados
conexao = sqlite3.connect(r'D:\Desenvolvimento\python\My-Finance-QtDesigner\database\database.db')
cursor = conexao.cursor()

# Ler o arquivo CSV com encoding alternativo (tente 'latin1' se 'utf-8' falhar)
with open(r'D:\desenvolvimento\python\My-Finance-QtDesigner\imports_outrem\cd_febraban.csv', mode='r') as file:
    reader = csv.reader(file)
    for linha in reader:
        # Verificar se a linha contém elementos
        print(linha)