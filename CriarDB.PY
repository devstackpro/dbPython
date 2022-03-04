
import pymysql

# Criar um objeto de conexão
databaseServerIP= "127.0.0.1"
databaseUserName = "root"
databaseUserPassword = "1234"
newDatabaseName = "TesteBase"
charSet = "utf8mb4"
cusrorType = pymysql.cursors.DictCursor

connectionInstance = pymysql.connect(
    host=databaseServerIP, 
    user=databaseUserName, 
    password=databaseUserPassword,
    charset=charSet,
    cursorclass=cusrorType)

try:
# Cria um objeto cursor
    cursorInsatnce = connectionInstance.cursor()                                    

# Instrução SQL para criar um banco de dados
    sqlStatement = "CREATE DATABASE "+newDatabaseName  

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
    connectionInstance.close()