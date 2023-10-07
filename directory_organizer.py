'''
Script by Bryan Tait, 10/6/2023
Note: This script was made to parse the Windows file format. 
This script will not work as intended with an OS with a different format for files
'''


#TODO: 
#     Make the script robust, currently it shall fail if a folder of a matching name already exists during folder creation
#     Make a graphical wrapper for

import os
import shutil
# list of files in current directory
currDir = os.listdir('.')
# list to cache seen filetypes
fileTypes = {}
# iterates through currDir, creating a folder for each file type
# then places each file of that type into the corresponding folder(corresponding on file type)
for file in currDir:
    # find the rightmost "." which in the case of windows is the delimiter before file type
    typeI = file.rfind('.')
    # if rfind couldn't find a "." delimiter, then it is not a file and should be skipped over
    if typeI == -1: continue
    # splice to isolate file ext, skipping over the "." delimiter
    ext = file[typeI+1:]
    
    # if ext does not already exist in dictionary then add it to dictionary and create folder
    if not ext in fileTypes:
        fileTypes[ext] = ext
        # os methods will resolve "." to the current directory
        path = ".\\" + ext
        # check if folder already exists
        if not os.path.isdir(path):
            os.makedirs(path)
    # move file to apporiate folder
        newPath = ".\\" + ext
        shutil.move(file, newPath)
