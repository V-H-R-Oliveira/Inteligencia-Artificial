# RBC

Sistema RBC projetado em Python 3x e utilizando o banco de dados Sqlite3

Dependências - Instalar o sqlite3

iniciar:
- No terminal do Linux, digite:
    - sqlite3 \<database.db\> -- cria ou abre um banco de dados 
    - sqlite3> .read ./sql/createTables.sql -- Este comando deverá ser executado uma vez, após a criação do banco
    - sqlite3> select * from pesos; -- Exemplo de consulta, utilize o sql para manipular os dados no Sqlite3
- Para executar o RBC, digite no terminal: python3 main.py

Todo:
- Menu - Linkar;
- Similariedade Local e Global;
- Atualizar base após os cálculos;
- Testes.