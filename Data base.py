import sqlite3
# SQLITE was used since it is easy to use and simple enough for this project.


# USER PROFILE DATABASE
connect_userProfile = sqlite3.connect('xProfile.db')    # Connecting database file to python file

c = connect_userProfile.cursor()    # Creating database with columns
c.execute("""
    CREATE TABLE IF NOT EXISTS UserProfile(
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL)
""")


# CONTENT MANAGEMENT DATABASE
connect_userContent = sqlite3.connect('xContent.db')    # Connecting database file to python file

c = connect_userContent.cursor()    # Creating database with columns
c.execute("""
    CREATE TABLE IF NOT EXISTS UserContent(
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    platform TEXT NOT NULL)
""")
