import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database library")
print("Database created successfully.")'''
'''mycursor.execute("create table libraries (id int(2) primary key Auto_Increment, book_name varchar (155), author varchar(155), genre varchar(150), series_no varchar(120), book_no varchar(110)")
print("Table created successfully.")
mycursor= mydb.cursor()'''
'''sql ="insert into libraries ( id, book_name, author, genre, series_no, book_no) values(%s,%s,%s,%s,%s)"
val=[
    ('',"data structure","Anuradha A. Puntambekar","Computer Science","34","01"),
    ('',"algorithm","Thomas H Cormen","Computer Science","22","02"),
    ('',"Operating System","Vijay Sukhla","Computer System","34","00")
    ]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
mycursor.execute("select * from library")
result=mycursor.fetchall()
for x in result:
    print(x)'''
