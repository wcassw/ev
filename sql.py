# sql.py - Create a SQLite3 table and populate it with data
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('evapp.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE evapp(title TEXT, description TEXT)')

    # insert dummy data into the table
    # c.execute('INSERT INTO evapp VALUES("Good", "I\'m good.")'
    
    # commit the changes
    c.commit()
