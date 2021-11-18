# File created from following resource: https://www.opentechguides.com/how-to/article/python/59/files-containing-text.html
import os
from pathlib import Path

class fileSearch:

    def fileSearchPath():

        # print(str(Path.home() / "Downloads"))
        # print(os.path.dirnmae(__file__) / "testingProject")
        # downloads_Directory = str(os.path.dirname(__file__))
        # search_path = downloads_Directory + "/testingProject"

        search_path = str(Path.home() / "Downloads")
        file_type = [".yaml", ".yml", ".csv"]
        search_str = ["replicaCount:", "datadog:", "datadogAgents:", "podAnnotations:", "kind: DaemonSet", "kind: Deployment", "AWSTemplateFormatVersion:", "Average Custom Metrics / Hour", "init_config:"]

        # Append a directory separator if not already present
        if not (search_path.endswith("/") or search_path.endswith("\\") ): 
                search_path = search_path + "/"
                                                                
        # If path does not exist, set search path to current directory
        if not os.path.exists(search_path):
                search_path =str(Path.home() / "Downloads")

        # Repeat for each file in the directory  
        for fname in os.listdir(path=search_path):
            
            fileDirectory = search_path + fname
            # Apply file type filter   
            print("test")
            for fileType in file_type:
                if fname.endswith(fileType):

                    # Open file for reading
                    fo = open(fileDirectory)
                    # Read the first line from the file
                    line = fo.readline()

                    # Loop until EOF
                    while line != '' :
                            # Search for string in line
                            for element in search_str:
                                index = line.find(element)
                                if ( index != -1) :

                                    if(os.path.exists(search_path + fname)):
                                        print(fileDirectory + " file deleted")
                                        os.remove(search_path + fname)

                            # Read next line
                            line = fo.readline()  

                    fo.close()

    if __name__ == '__main__':
        fileSearchPath()