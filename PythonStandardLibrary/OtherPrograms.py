import subprocess

# capture output makes it not display results on the terminal
completed = subprocess.run(["ls", "-l"])

# run another python script
completed2 = subprocess.run(["python3", "ComplexScript.py"])
