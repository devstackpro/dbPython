
import pymysql

# Criar um objeto de conexão
my_database = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    db='TesteBase', 
    charset='utf8mb4')
cursor = my_database.cursor()

try:
# Cria um objeto cursor
    cursorInsatnce = my_database.cursor()                                    

# Instrução SQL para criar um banco de dados
    sqlStatement = "CREATE TABLE Teares(id int, LastName varchar(9), FirstName varchar(9), DepartmentCode int)"

# Execute a instrução SQL de criação de banco de dados por meio da instância do cursor
    cursorInsatnce.execute(sqlStatement)

# Cadeia de consulta SQL
    sqlQuery = "SHOW DATABASES"

# Execute the sqlQuery
    cursorInsatnce.execute(sqlQuery)

# Pegue todas as linhas
    databaseList = cursorInsatnce.fetchall()
 
    for datatbase in databaseList:
        print(datatbase)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    my_database.close()