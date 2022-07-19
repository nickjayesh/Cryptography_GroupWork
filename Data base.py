import sqlite3
# SQLITE was used since it is easy to use and simple enough for this project.


# USER PROFILE DATABASE
connect_userProfile = sqlite3.connect('APP database.db')    # Connecting database file to python file

c = connect_userProfile.cursor()    # Creating database with columns
c.execute("""
    CREATE TABLE IF NOT EXISTS UserProfile(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL)
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS UserContent(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    platform TEXT NOT NULL)
""")
