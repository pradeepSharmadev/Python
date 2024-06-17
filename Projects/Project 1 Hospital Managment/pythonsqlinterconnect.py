import mysql.connector
try:
    mydb = mysql.connector.connect(host="127.0.0.1",user="root",password='databasepassw')
    mycur = mydb.cursor()
    if mydb.is_connected():
        print("success")
except Exception as e:
    print ("error",e)