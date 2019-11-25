# RBC

Sistema RBC projetado em Python 3x e utilizando o banco de dados Sqlite3.

A base de dados já vem preparada, portanto, é só executar: python3 main.py

Dependências - Sqlite3 (sudo apt install sqlite3)

Caso não possua um rbc.db:
- No terminal do Linux, digite:
    - sqlite3 \<database.db\> -- cria ou abre um banco de dados 
    - sqlite3> .read ./sql/createTables.sql
    - sqlite3> .exit
    - python3 fillDatabase.py

Para executar os testes:
- python3 main.py \< test/case\<numero\>.in

No arquivo .in da pasta test:
- As linhas 37 e 38 devem ser alteradas para poder salvar ou atualizar;