from pathlib import Path
from zipfile import ZipFile

# coping contents of all files in the ecommerce directory into a zip file
# using rglob to recursively find all files that end with "."

# for path in Path("ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()

with ZipFile("file.zip") as zip:
    print(zip.namelist())


