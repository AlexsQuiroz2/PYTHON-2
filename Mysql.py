import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
)

mycursor = mydb.cursor()
mycursor.execute("USE midatabase")


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)