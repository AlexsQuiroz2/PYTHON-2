import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database="midatabase"
)

mycursor = mydb.cursor()

'''mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")'''
'''mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")'''
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)