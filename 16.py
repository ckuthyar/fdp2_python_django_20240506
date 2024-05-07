import mysql.connector as mc
conne=mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="4mw20cs"
)
cursor2=conne.cursor()
cursor2.execute("select * from employee")
for i in cursor2:
    print(i)
