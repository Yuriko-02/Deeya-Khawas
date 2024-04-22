import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database inventory")
print("Database created successfully.")'''
'''mycursor.execute("create table inventory(id int(2) primary key Auto_Increment, item_name varchar (155), item_quantity varchar(155), item_type varchar(150), date varchar(120)")
print("Table created successfully.")'''
mycursor= mydb.cursor()
'''sql ="insert into inventory ( id, item_name, item_quantity, item_type, date) values(%s,%s,%s,%s,%s)"
val=[
    ('',"desk","4","wooden","21/4/23"),
    ('',"bench","8","wooden","21/4/23"),
    ('',"tea set","10","glass","22/4/23")
    ]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
mycursor.execute("select * from inventory")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from inventory where item_name ='desk'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
    