import sqlite3
import json
from pathlib import Path
from PythonStandardLibrary.JSON import movies

# movies = json.loads(Path("movies.json").read_text())


# print(movies)

# if SQLite object called 'db' doesn't exist the connect function will create it
# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ? , ?)"

    # iterate over the movie list and execute the command for each item
    # for movie in movies:
    #     # put each set of key/values in a tuple
    #     connection.execute(command, tuple(movie.values()))
    # connection.commit()

# pulling from the database
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"

cursor = connection.execute(command)

for row in cursor:
        print(row)

