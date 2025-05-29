import csv
import sqlite3

conn = sqlite3.connect("zara.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'jcpicker','C:\\Users\\4000tu\\Downloads\\jcpicker.exe')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')"
# cursor.execute(query)
# conn.commit()

# cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)
#                ''')


# # Specify the column indices you want to import (0-based index)
# # Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
        
# # Commit changes and close connection
# conn.commit()
# conn.close()


# query = """UPDATE contacts
# SET name = "maa"
# WHERE id=4;
# """
# cursor.execute(query)
# conn.commit()


# query = 'kaushal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

# query = "CREATE TABLE IF NOT EXISTS memory(id integer primary key, info VARCHAR(100))"
# cursor.execute(query)

# cursor.execute("INSERT INTO memory (id, 'info') VALUES (null, 'my owner name is bhaik & kaushal')")
# conn.commit()

# cursor.execute("delete from sys_command")
# conn.commit()
    
# query = "CREATE TABLE IF NOT EXISTS personal_details(id integer primary key, email VARCHAR(100), password VARCHAR(20))"
# cursor.execute(query)

# cursor.execute("INSERT INTO personal_details (id, 'email', 'password') VALUES (null, 'bhavik@gmail.com', 'bhavik123')")
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS personal_details(id integer primary key,name VARCHAR(100), email VARCHAR(100), password VARCHAR(20), mo VARCHAR(100))"
# cursor.execute(query)

# cursor.execute("INSERT INTO personal_details (id, 'name','email', 'password','mo') VALUES (null, 'bhavik','bhavik@gmail.com', 'bhavik123','8469116598')")
# conn.commit()

cursor.execute("delete from personal_details")
conn.commit()

# cursor.execute("DROP TABLE personal_details;")
# conn.commit()