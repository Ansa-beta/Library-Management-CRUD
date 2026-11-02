from mysql import connector
import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Ansa@3272",
                database="library_db"
            )
            return self.connection
        except Exception as e:
            return None
class LibraryManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connection = super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from book"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="insert into book(title,author,category,price,published_date) values(%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New book added successfully...")
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            if records!=None:
                query="delete from book where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Book deleted successfully...")
            else:
                print("Book not found...")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update book set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Book details updated successfully")

            else:
                print("Book not found...")

        except Exception as e:
            print(e)

# connection_instance=DbConnect()
# print(connection_instance.get_connection())
#
book_instance=LibraryManager()
# book_instance.post(
#     title="The Alchemist",
#     author="Paulo Coelho",
#     category="Fiction",
#     price=300,
#     published_date=datetime.date(1988, 1, 1)
# )
book_instance.get()
print("------------")
book_instance.retrieve(id=2)
# book_instance.delete(id=1)
# print("---------------------")
book_instance.put(2,price=350)
# member_instance.get()