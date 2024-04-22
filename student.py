import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database student")
print("Database created successfully.")'''
'''mycursor.execute("create table student (id int(2) primary key Auto_Increment, name varchar (155), address varchar(155), phone varchar(10), contact_person varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
sql ="insert into student ( id, name, address, phone, contact_person) values(%s,%s,%s,%s,%s)"
val=[
    ('',"Deeya Khawas","Dilaram","6843843484","Mr. Sarban Khawas"),
    ('',"Twinkle Pradhan","Sonada","9873523178","Mr. Rajesh Pradhan"),
    ('',"Amar Rai","Panighata","6295996937","Mr. Sambhu Rai")
]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
