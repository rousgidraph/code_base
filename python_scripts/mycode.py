import sqlite3 as sql
from sqlite3.dbapi2 import Cursor

#sqlite will create a database file 


def create_database():
    conn = sql.connect('database.db')
    print("Database created successfully")
    conn.close()
    pass

def create_table():
    conn = sql.connect('database.db')
    print("database connected ")
    statement = "CREATE TABLE if not exists todo (ID INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(30), content varchar(300));" # the sql to be executed 
    conn.execute(statement)
    conn.close()

    pass


def insert_record(title,content):
    conn = sql.connect('database.db')
    print("database connected ")
    statement = "INSERT INTO todo (title,content) values('"+title+"','"+content+"')"
   
    conn.execute(statement)
    
    conn.commit()
    print('Record added successfully')
    conn.close()
    pass

def update_record(id,title,content):
    
    conn = sql.connect('database.db')
    print("database connected ")
    statement = "UPDATE todo set title = '"+title+"', content='"+content+"' where ID = "+id
    conn.execute(statement)
    print("rows affected ", conn.total_changes)
    conn.commit()
    conn.close()

    pass

def delete_record(id):
    read_all()
    conn = sql.connect('database.db')
    print("database connected ")
    statement = "DELETE FROM todo where ID = "+id
    conn.execute(statement)
    print("rows affected ", conn.total_changes)
    conn.commit()
    conn.close()
    read_all()
    pass

def read_all():
    conn = sql.connect('database.db')
    print("database connected ")
    statement = "SELECT * FROM todo"
    cursor= conn.execute(statement)
    for row in cursor:
        print ("id :",row[0])
        print("Title :", row[1])
        print("Content :", row[2])
        print("\n")
    conn.close()
    print("records read successfully")
    pass


def driver():
    print("Welcome to my todo list app\n")
    choice = 0
    while(choice != 6):
        choice = int(input("\n\nHere are the avilable options \n1. initialize the app \n2. new todo item \n3. show me my todo\n4. update an item \n5. delete an item \n6.Exit \nEnter the correponding number:"))
        if choice == 1:
            create_database()
            create_table()
        if choice == 2:
            title = input("What should be the title :")
            cont = input("ENter the content :\n")
            insert_record(str(title),str(cont))

        if choice == 3:
            read_all()
        if choice == 4:
            read_all()
            change_id = input("The id of the item you want to change : ")
            change_title = input("The new title : ")
            change_content = input("THe new content \n:")
            update_record(change_id,str(change_title),str(change_content))
            read_all()
        if choice == 5:
            read_all()
            del_id = input("the id if the item to delete : ")
            delete_record(del_id)
            read_all()

    pass

if __name__ == "__main__":
   
   
    driver()