'''
Start imports
'''
import os

'''
Definitions used
'''
### creates a dirrectory if one does not exist
def creat_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

### Open a file for writing and dumps the data in
def write_file(path, data):
    file = open(path, "w")
    file.write(data)
    file.close