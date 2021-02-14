import shutil
from pathlib import Path

from PythonStandardLibrary import ecommerce

path = Path("ecommerce/new.txt")
target = Path("ecommerce")

# can use the shell util library for high level directory commands
shutil.copy(path, target)