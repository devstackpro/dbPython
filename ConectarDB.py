import pymysql

# ACESSAR O BANCO DE DADOS 
my_database = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    db='mysql', 
    charset='utf8mb4')
cursor = my_database.cursor()

# EXIBIR BANCO DE DADOS 
cursor.execute("show databases")
for db in cursor:

  print(db)

