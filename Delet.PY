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
    cursorInstance = my_database.cursor()  

# SQL statement for deleting rows from a table matching a criteria
    sqlDeleteRows   = "ALTER TABLE TESTE DROP DepartmentCode"
    my_database.commit()
# using the cursor delete a set of rows from the table
    cursorInstance.execute(sqlDeleteRows)

# Check if there are any existing items with expired status
    sqlSelectRows   = "select * from teste "

# Execute the SQL query
    cursorInstance.execute(sqlSelectRows)

# Fetch all the rows using cursor object
    itemRows = cursorInstance.fetchall()

# print all the remaining rows after deleting the rows with status as "expired"
    for item in itemRows:
        print(item)   

except Exception as ex:
    print("Exception occured: %s"%ex)   

finally:
    my_database.close()