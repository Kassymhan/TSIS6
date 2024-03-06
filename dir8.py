import os

path = "/Users/kasymhan2005/Documents/PP2/A.txt"

if os.access(path, os.F_OK) and os.path.exists(path):
    os.remove(path)