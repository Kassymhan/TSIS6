import os


path = r"/Users/kasymhan2005/Documents/PP2/t.txt"

if os.path.exists(path):
    print("exists")

    print(os.path.split(path))