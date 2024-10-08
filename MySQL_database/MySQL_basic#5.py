import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practicebase"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS practicebase")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies(
        Id INT PRIMARY KEY,
        Titles VARCHAR(64),
        Directors VARCHAR(64),
        Years INT,
        Length_minutes INT
    );
""")

cursor.execute("""
    INSERT IGNORE INTO movies (Id, Titles, Directors, Years, Length_minutes) VALUES
    (1, 'Toy Story', 'John Lasseter', 1995, 81),
    (2, 'A Bug''s Life', 'John Lasseter', 1998, 95),
    (3,	'Toy Story 2', 'John Lasseter',	1999, 93),
    (4,	'Monsters, Inc.', 'Pete Docter', 2001, 92),
    (5,	'Finding Nemo',	'Andrew Stanton', 2003, 107),
    (6,	'The Incredibles', 'Brad Bird',	2004, 116),
    (7,	'Cars',	'John Lasseter', 2006, 117),
    (8,	'Ratatouille', 'Brad Bird', 2007, 115),
    (9,	'WALL-E', 'Andrew Stanton', 2008, 104),
    (10, 'Up', 'Pete Docter', 2009, 101),
    (11, 'Toy Story 3',	'Lee Unkrich', 2010, 103),
    (12, 'Cars 2', 'John Lasseter', 2011, 120),
    (13, 'Brave', 'Brenda Chapman', 2012, 102),
    (14, 'Monsters University', 'Dan Scanlon', 2013, 110);
""")
conn.commit()


cursor.execute("SELECT * FROM movies")
result1 = cursor.fetchall()
for i in result1:
    print(i)
print()

cursor.execute("SELECT titles FROM movies")
result2 = cursor.fetchall()
for i in result2:
    print(i)
print()

cursor.execute("SELECT directors FROM movies")
result3 = cursor.fetchall()
for i in result3:
    print(i)
print()

cursor.execute("SELECT id, titles, directors FROM movies")
result4 = cursor.fetchall()
for i in result4:
    print(i)
print()

cursor.execute("SELECT id, titles, years FROM movies")
result5 = cursor.fetchall()
for i in result5:
    print(i)
print()

cursor.close()
conn.close()
