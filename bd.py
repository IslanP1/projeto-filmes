import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="biblioteca-flask",
        user='postgres',
        password='123456')

# Abra um cursor para realizar operações de banco de dados
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Filmes;')
cur.execute('CREATE TABLE Filmes (id serial PRIMARY KEY,'
                                 'nome varchar (150) NOT NULL,'
                                 'genero varchar (50) NOT NULL,'
                                 'autor varchar (150) NOT NULL,'
                                 'resenha varchar (150) NOT NULL);'
                                 )

cur.execute('DROP TABLE IF EXISTS Usuarios;')
cur.execute('CREATE TABLE Usuarios (id serial PRIMARY KEY,'
                                 'nome varchar (150) NOT NULL,'
                                 'username varchar (30) NOT NULL,'
                                 'senha varchar (30) NOT NULL);'
                                 )

conn.commit()
cur.close()
conn.close()