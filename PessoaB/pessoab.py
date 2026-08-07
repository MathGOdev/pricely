import sqlite3

conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()

#Parte do Banco de Dados
cursor.execute("""
    CREATE TABLE IF NOT EXISTS precos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        preco REAL NOT NULL,
        data_coleta TEXT NOT NULL
    )
""")

conexao.commit()

print("Banco de dados conectado.")
print("Tabela 'precos' pronta para uso.")