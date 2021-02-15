import json
from pathlib import Path

# make a dictionary of movies
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "School of Rock", "year": 1993}
]


# store json dump into movies_json variable
movies_json = json.dumps(movies)

# create movies.json file and write contents of json variable to the file
Path("movies.json").write_text(movies_json)

# make new variable with the contents of the json file created and store in variable
data = Path("movies.json").read_text()

# print iterated values of the variables with .loads() function

print(json.loads(data))

