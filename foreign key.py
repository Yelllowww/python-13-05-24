import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1')
    print('Conexão_db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = '''CREATE DATABASE if not exists db_cadastro'''
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print("\nConexão fechada")

def create_connection():
    conexao = mysql.connector.connect(user='root',
                                        password='',
                                        host='127.0.0.1',
                                        database='db_cadastro')
    print('Conexão:', conexao)
    return conexao

def create_table():
    create = '''CREATE TABLE if not exists tb_cargo(
                idt INT NOT NULL AUTO_INCREMENT,
                cargo VARCHAR(20) UNIQUE NOT NULL,
                PRIMARY KEY(idt))'''
    cursor.execute(create)

    create2 = '''CREATE TABLE if not exists funcionario(
                matricula INT NOT NULL AUTO_INCREMENT,
                nome CHAR(50) NOT NULL,
                dt_nascimento DATE,
                genero ENUM('m','f') NOT NULL,
                cd_cargo INT NOT NULL, 
                PRIMARY KEY(matricula),
                FOREIGN KEY(cd_cargo) REFERENCES tb_cargo(idt))'''
    cursor.execute(create2)

def insert_cargo():
    insert = '''INSERT INTO tb_cargo (cargo) VALUES('programador')'''
    cursor.execute(insert)
    conexao.commit()
def insert_empregado():
    insert2 = '''INSERT INTO funcionario(nome,dt_nascimento,genero,cd_cargo) 
                VALUES('Eduardo','2050-05-10','m',1)'''
    cursor.execute(insert2)
    conexao.commit()

def delete():
    delete = '''DELETE FROM funcionario WHERE nome = 'Eduardo' '''
    cursor.execute(delete)
    conexao.commit()

def delete_cargo():
    delete = '''DELETE FROM tb_cargo WHERE idt = 1 '''
    cursor.execute(delete)
    conexao.commit()

def select():
    select = '''SELECT * FROM funcionario'''
    cursor.execute(select)
    registros = cursor.fetchall()
    for i in registros:
        print(i)

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada')

if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_cargo()
    insert_empregado()
    #delete()
    #delete_cargo()
    select()
    close_connection()
