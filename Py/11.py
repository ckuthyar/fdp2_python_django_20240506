import mysql.connector as mc

conn1=mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="4mw20cs"
)

rows=conn1.execute("select * from employee")
print(rows)
conn1.close()
