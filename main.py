import os
from pathlib import Path
import shutil

def main():
    #This will delete any .zip files in your downloads folder where datadog-agent is part of the path
    zipFlareName = "datadog-agent"
    extension = ".zip"
    search_path = str(Path.home() / "Downloads")

    #removeExtractedFlares()

    #check whether path exists and is a directory
    if os.path.exists(search_path):
        if os.path.isdir(search_path):
            # iterating through the subfolders
            for root, dirs, files in os.walk(search_path):
                for name in files:
                    # get the file path
                    file_path = os.path.join(root, name)

                    # extract the extension from the filename
                    file_extension = os.path.splitext(file_path)[1]

                    #Check if the file_extension is a zip
                    if extension == file_extension:
                        #Check that the file_path contains zipFlareName - could improve
                        if zipFlareName in file_path:
                        # Delete the file
                            if not os.remove(file_path):
                                # success message
                                print("File deleted successfully")
                                
                            else:
                                # failure message - possibly permissions issue
                                print("Unable to delete the file")
                        else:
                            print("File is not a flare")
        else:
            print(f"{search_path} is not a directory")
    else:
        print(f"{search_path} does not exist")

def removeExtractedFlares():
    """"
    #lets set a static path until we get Kumail's section
    #path is inside an extracted flare; the name is unimportant here
    static_path = "/Users/venus.parfait/Downloads/saltabcc104_pat_csl_cloud_td_com 2/status.log"

    #also set statically until Kumail's part
    statusLogPresent = True
    
    #if directory contains a status log we know the parent directory is an extracted flare
    if statusLogPresent:
        #do work

        #Split our path string based on the /'s 
        #This will assume that the path of an extracted flare follows the format: /Users/<user>/Downloads/<flare_name>
        splitPath = static_path.split("/")

        print(f"{static_path} path before splitting")
        print(f"{splitPath} path after splitting")
        #returns a list of 6 strings remove the first and last entry

        #drop the first and last entry
        print(splitPath[1:5])
    """""
    
    #entire code section needs to be wrapped
    #kumies code
    startPath = str(Path.home() / "Downloads")
    file_name = ["status.log", "cluster-agent-status.log"]

    #check if there is a slash at the end of path, if not add one
    if not (startPath.endswith("/") or startPath.endswith("\\") ): 
        startPath = startPath + "/"

    #Check if current path exists
    if os.path.exists(startPath):
        #fname is each filename within the folder (startPath)
        for fname in os.listdir(startPath):
            fileDirectory = startPath + fname
            for fileType in file_name:
                    if fileType in fname:
                        #file directory is the full path
                        #CHECK THIS LATER
                        if(os.path.exists(fileDirectory)):                        
                            #Split our path string based on the /'s 
                            #This will assume that the path of an extracted flare follows the format: /Users/<user>/Downloads/<flare_name>
                            splitPath = fileDirectory.split("/")

                            #Drop the first and last entry
                            slicedPath = splitPath[1:5]

                            #Now we remake the path and remove the file
                            pathToRemove = "/" + slicedPath[0] + "/" + slicedPath[1] + "/" + slicedPath[2] + "/" + slicedPath[3]
                            shutil.rmtree(pathToRemove)

    else:
        print(f"{startPath} does not exist")

        


if __name__ == '__main__':
    main()
