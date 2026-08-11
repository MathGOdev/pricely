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

def inserir_preco(dado):
    cursor.execute(
        "INSERT INTO precos (produto, preco, data_coleta) VALUES (?, ?, ?)",
        (dado["produto"], dado["preco"], dado["data_coleta"])
    )
    conexao.commit()
    print(f"Preço de '{dado['produto']}' salvo: R$ {dado['preco']}")

print("Banco de dados conectado.")
print("Tabela 'precos' pronta para uso.")

# Teste - simula o que a Pessoa A vai entregar
dado_teste = {
    "produto": "Notebook Dell",
    "preco": 3499.90,
    "data_coleta": "2026-08-11"
}

inserir_preco(dado_teste)