#File created from following resource: https://www.opentechguides.com/how-to/article/python/59/files-containing-text.html

#Import os module
import os
from pathlib import Path
import re

# Ask the user to enter string to search

#print(str(Path.home() / "Downloads/testingProject"))
#print(os.path.dirname(__file__) / "testingProject")

# Testing purposes using the folderpath for project
# search_path = str(Path.home() / "Downloads")

# REQUIRED TO ADD TESTING FILES IN testingProject repo
search_path = str(os.path.dirname(__file__)) + "/testingProject"
file_type = input("File Type : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path =str(Path.home() / "Downloads")

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):

   # Apply file type filter   
   if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :

                    #print(fname, "[", line_no, ",", index, "] ", line, sep="")
                    
                    #os.remove(search_path + fname)
                    print(search_path + fname + " file deleted")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()