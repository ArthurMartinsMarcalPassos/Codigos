import sqlite3

with sqlite3.connect("arquivo txt") as c:
    
    cur = c.cursor()

    sql = """

        CREATE TABLE IF NOT EXISTS 
        ALUNO(
            ID INTEGER NOT NULL (ID AUTOINCREMENT) 
            NOME TXT NOT NULL,
            PRIMARY KEY 
            );,
"""

    c.execute (sql)

    sql = """
     
        CREATE TABLE IF NOT EXISTS
        DISIPLINA (
            ID INTERGER NOT NULL (ID AUTOINCREMENT),
            NOME TXT NOT NULL,
            PRIMARY KEY 
        );
"""
    c.execute (sql)

    sql = """
        INSERT INTO  ALUNO(NOME)VALUES
        ('yuri')
    """
    nome = input("Digite seu nome.")
    c.execute(sql,{"nome":nome})
    for  i in cur.fetchall():
        print(i)