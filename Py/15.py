import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="user",
  passwd ="root"
  database="4mwcs20"
)
 
print(dataBase)
  
# Disconnecting from the server
dataBase.close()
