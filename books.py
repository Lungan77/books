import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lungan@7@7",
  database='LibrarySystem'
)

mycursor = mydb.cursor()

def add_books(Title, Author, YearPublished):
    sql = "INSERT INTO books(title, auther, yearpublished) VALUES(%s, %s, %s)"
    val = (Title, Author, YearPublished)
    mycursor.execute(sql, val)
    mydb.commit()

def view():
    sql = "SELECT * FROM books"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def update(book_id, title=None, author=None, year_published=None):
    # SQL to check if the book exists
    sql = "SELECT * FROM books WHERE bookID = %s"
    Id = (book_id, )
    
    # Execute the SQL command
    mycursor.execute(sql, Id)
    
    # Fetch the result
    book = mycursor.fetchone()

    # Check if the book exists
    if book:
        updates = []
        params = []

        # Prepare updates if parameters are provided
        if title:
            updates.append("title = %s")
            params.append(title)
        
        if author:
            updates.append("author = %s")
            params.append(author)
        
        if year_published:
            updates.append("yearPublished = %s")
            params.append(year_published)

        # If there are updates, execute the update SQL
        if updates:
            update_sql = f"UPDATE books SET {', '.join(updates)} WHERE bookID = %s"
            params.append(book_id)
            mycursor.execute(update_sql, params)
            mydb.commit()  # Don't forget to commit changes
            print("Book updated successfully!")
        else:
            print("No fields to update.")
    else:
        print("Book not found.")

# Usage example
# update(1, title="New Title", author="New Author", year_published=2023)




def delete(id):
    sql = "DELETE FROM books WHERE bookID = %s"
    Id = (id, )
    mycursor.execute(sql, Id)
    mydb.commit()

view()
delete('1')
view()
