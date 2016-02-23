import os
import zipfile

with zipfile.ZipFile('namesbystate.zip') as namesbystate:
    for filename in namesbystate.namelist():
        if not os.path.isdir(filename):
            # read the file
            with namesbystate.open(filename) as f:
                for line in f:
                    print line
