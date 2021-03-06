"""This is a script to practice SQL in Python"""
#TODO


#VCS --> import into VCS --> create Git Repository
# manually reate reposiry in github using same name as porject
# VCS commit, paste the repository URL

# Python code to demonstrate table creation and insertions with SQL. run first part, then comment it and run 2nd part.

import sqlite3


########## FIRST PART #################
# # connecting to the database
# connection = sqlite3.connect("myTable.db")
#
# # cursor
# crsr = connection.cursor()
#
# # SQL command to create a table in the database
# sql_command = """CREATE TABLE emp (
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE);"""
#
# # execute the statement #--> get error if execute this for second time
# crsr.execute(sql_command)
#
# # SQL command to insert the data in the table
# sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
# crsr.execute(sql_command)
#
# # another SQL command to insert the data iconnection n the table
# sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");""" # --> can use ? as placeholder as cursor.execute('''INSERT INTO users(name, phone, email, password)
#                                                                                                                       VALUES(?,?,?,?)''', (name2,phone2, email2, password2)) here passing the values
#                                                                                                        a tuple or can pass the values as dictionary --> cursor.execute('''INSERT INTO users(name, phone, email, password)
#                                                                                                                                                            VALUES(:name,:phone, :email, :password)''',
#                                                                                                                                                           {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})

# crsr.execute(sql_command)
#
# # To save the changes in the files. Never skip this.
# # If we skip this, nothing will be saved in the database.
# connection.commit()
#
# # close the connection
# connection.close()





# Python code to demonstrate SQL to fetch data.

import sqlite3

############## SECOND PART #################
# connect withe the myTable database
connection = sqlite3.connect("myTable.db")

# cursor object
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM emp") #--> to retrieve data execute from cursor. use fecthone() or fetchall()

# cursor.execute('''SELECT name, email, phone FROM users''')
# user1 = cursor.fetchone() #retrieve the first row
# all_rows = cursor.fetchall()
# To retrieve data with conditions, use again the "?" placeholder:
#     cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
#     user = cursor.fetchone()


# store all the fetched data in the ans variable
ans = crsr.fetchall()

# loop to print all the data
for i in ans:
    print(i)