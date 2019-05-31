import sqlite3

conn = sqlite3.connect('shallownowschool.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE tb_estudante(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(30)NOT NULL,
endereço TEXT NOT NULL,
nascimento DATE NOT NULL,
matrícula VARCHAR (12) NOT NULL
);
""")
print ("Tabela tb_estudante tabela criada com sucesso!")
conn.close()

-----------------------------------------------------------------------

import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()
valores = [('José', 'Rua Costa Beriz', '2000-02-29', '201510013210')]

cursor.executemany("""
    INSERT INTO tb_estudante(nome, endereço, nascimento, matrícula)
    VALUES(?, ?, ?, ?);
""", valores)

conn.commit()

print ("Valores inseridos com sucesso e shallow now!")

conn.close()
----------------------------------------------------------------------------
