import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
   " test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)               #will give the path of the file depending on windows, linux, or mac
    filedir, filename = os.path.split(filepath)     #will split the file directory and file itself

    if filedir !="":                                #for creating the folder -> checking whether empty
            os.makedirs(filedir, exist_ok=True)     #if not empty, create the folder
            logging.info(f"Creating directory; {filedir} for the file: {filename}")         #log message

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):              #if the filepath has been created or not
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")