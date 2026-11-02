from mysql import connector
import datetime

class LibraryManager:
    def __init__(self):
        self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Ansa@3272",
            database="library_db"
        )
        print("Connected Successfully..!")

    def get_object(self, id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""insert into book
            (title,author,category,price,published_date)
            values(%s,%s,%s,%s,%s)"""
            values=[v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Book added successfully")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            return record
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record!=None:
                print(record)
            else:
                print("Book not found...")
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record!=None:
                query="delete from book where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Book deleted successfully...")
            else:
                print("Book not found..")
        except Exception as e:
            print(e)

    def put(self, id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(", ")
                query=f"update book set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Book details updated successfully")
            else:
                print("Book not found...")
        except Exception as e:
            print(e)

book_instance = LibraryManager()
# book_instance.LibraryManager()
# book_instance.post(title="Wings of Fire",author="APJ Abdul Kalam",category="Biography",price=250,published_date=datetime.date(1999, 1, 1)
print(book_instance.get())

print(book_instance.get_object(id=1))
# book_instance.retrieve(id=1)
# book_instance.delete(id=1)
# book_instance.put(1, price=300)
# print(book_instance.get())
