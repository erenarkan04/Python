from ctypes import Array
from pathlib import Path
from time import ctime

Path().home()

Path("/usr/local/bin")

path = Path("ecommerce")
filepath = Path("ecommerce/new.txt")

print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.parent)

# returns a new path with the same object but a different name
path2 = path.with_name("file.txt")
# same with a different suffix
path3 = path.with_suffix(".txt")
print(path3)

# path.mkdir()
# path.rmdir()
# path.rename("ecommerce")

for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir()]
print(paths)

# glob or rglob (recursive glob) can be used to filter items
paths2 = [p for p in path.glob("*.py")]
print(paths2)

paths3 = [p for p in path.rglob("*.py")]
print(paths3)

# use ctime function to get human readable time of the time file was created
print(ctime(path.stat().st_ctime))

print(filepath.write_text("abcabc test"))

print(filepath.read_text())
