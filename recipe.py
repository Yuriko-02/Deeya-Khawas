import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="recipe"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database recipe")
print("Database created successfully.")'''
'''mycursor.execute("create table recipe ( id int(2) primary key Auto_Increment,name varchar (155), ingredients varchar(155), instruction varchar(150), time varchar(120), difficulty varchar(10)")
print("Table created successfully.")'''
mycursor= mydb.cursor()
'''sql ="insert into recipe (id,  name, ingredients, instruction, time, difficulty) values(%s,%s,%s,%s,%s)"
val=[
    ('',"candy","sugar,water,flavourings","melt sugar add water and flavourings and cool it down","5-6 mins","easy"),
    ('',"ice cream","milk,vanilla extract","mix milk and vanilla extrat and freeze it","10-15 mins","easy"),
    ('',"chicken soup","chicken,onion,garlic,ginger,water","boil all of them in water add salt according to taste","15-30 mins","medium")
]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
'''