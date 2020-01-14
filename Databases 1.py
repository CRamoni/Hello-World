import sqlite3
#database setup
db=sqlite3.connect('books_db')
cursor=db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty TEXT)''')
db.commit()

## Add function
def add_():
    id1 =int(input("Enter the book id: "))
    title = input("Enter the book Title: ")
    autha = input("Enter the book Author: ")
    qty = int(input("Enter the book qty: "))

    books = [(id1, title, autha, qty)]
    cursor.executemany('''INSERT INTO books(id,Title, Author, Qty)VALUES(?,?,?,?) ''', books)
    print("The following book has been added to books table:\n\n",books)
    db.commit()

## Update function
def update_():

    u = int(input("To update a book, Enter the book id: "))
    v = str(input("Change the books Title :"))
    cursor.execute(f'''UPDATE books SET Title = "{v}" WHERE id = {u}''')
    db.commit()
    
    cursor.execute('''SELECT * FROM books WHERE id = "{u}" ''')
    books = cursor.fetchone() 
    print(books)
    

##code for updating db

##Delete Function
def delete_():
    cursor.execute('''SELECT * FROM books ''')
    books = cursor.fetchall()
    print(books)
    g = int(input("To delete a book, enter its ID :"))
    cursor.execute(f'''DELETE FROM books WHERE id ={g}''')
    print("Book successfully deleted!\n")
    db.commit()

##Search function
def search_():
    cursor.execute('''SELECT * FROM books ''')
    books = cursor.fetchall()
    print(books)

    h = int(input("Enter ID to search for a book :"))
    cursor.execute(f'''SELECT * FROM books WHERE id ={h}''')
    books = cursor.fetchone()
    print(books)
   
##menu
def menu_():
        while True:
            u = int(input("What Would you like to do : \n 1. Enter Book \n 2. Update Book \n 3. Delete Book \n 4. Search \n 0. Exit \n"))
            if u == 1:
                add_()#Call the corresponding function based on menu option 
            elif u == 2:
                update_()
            elif u == 3:
                delete_()
            elif u == 4:
                search_()
            elif u == 0: #User can break out of loop 
                break
            else :
                 print("Invalid input")
menu_()
#inserting into books
sql_command = """INSERT INTO books (id,title,author,qty)
    VALUES (3001,'A Tale of two Cities','Charles Dickens',30\n);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO books (id,title,author,qty)
    VALUES (3002,"Harry Potter and the Philosopher's Stone","J.K. Rowling",40\n);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO books (id,title,author,qty)
    VALUES (3003,"The Lion, the Witch and the Wardrobe","C.S. Lewis",25);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO books (id,title,author,qty)
    VALUES (3004,"The Lord of the Rings","J.R.R. Tolkien",37);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO books (id,title,author,qty)
    VALUES (3005,"Alice in Wonderland","Lewis Carroll",12);"""
cursor.execute(sql_command)

db.commit()

cursor = db.cursor()
cursor.execute('''SELECT *FROM books''')
record = cursor.fetchall()
print("The books table contains the following books:",'\n',record)


