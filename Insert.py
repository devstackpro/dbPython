import pymysql
import pymysql.cursors

# Criar um objeto de conexão
my_database = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    db='TesteBase', 
    charset='utf8mb4')
cursor = my_database.cursor()

try:
# Criar um objeto de cursor
    cursorObject = my_database.cursor()                                     

# String SQL para criar uma tabela MySQL
    #sqlCreateTableCommand = "CREATE TABLE teste(id int(11) AUTO_INCREMENT PRIMARY KEY, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"

# Execute the sqlQuery
    #cursorObject.execute(sqlCreateTableCommand)

# Listar as tabelas usando o comando SQL
    #sqlShowTablesCommand = "show tables"   

# Execute the SQL command
    #cursorObject.execute(sqlShowTablesCommand)

# Busque todas as linhas - da saída do comando
    #rows = cursorObject.fetchall()
    #for row in rows:
        #print(row)

# Inserir linhas na tabela MySQL
    insertStatement = "INSERT INTO teste (id, LastName, FirstName, DepartmentCode) VALUES (3,'Albert','Einstein',10);"   
    cursorObject.execute(insertStatement)
    my_database.commit()

# Obter o valor da chave primária da última linha inserida
    print("Primary key id of the last inserted row:")
    print(cursorObject.lastrowid)

# SQL Query to retrive the rows
    sqlQuery = "select * from teste"   

# Buscar todas as linhas - para a consulta SQL
    cursorObject.execute(sqlQuery)
    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    my_database.close()




    