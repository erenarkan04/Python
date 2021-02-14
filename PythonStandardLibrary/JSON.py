import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "School of Rock", "year": 1993}
]

movies_json = json.dumps(movies)

Path("movies.json").write_text(movies_json)
