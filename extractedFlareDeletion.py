import os
from pathlib import Path
import shutil

def removeExtractedFlares():
    startPath = str(Path.home() / "Downloads")
    file_name = ["status.log", "cluster-agent-status.log"]

    #check if there is a slash at the end of path, if not add one
    if not (startPath.endswith("/") or startPath.endswith("\\") ): 
        startPath = startPath + "/"

    for root, dirs, files in os.walk(startPath):
        #this is each directory
        for name in dirs:

            targetPath = startPath + name + "/"

            #Check if current path exists
            if os.path.exists(targetPath):
                #fname is each filename within the folder (startPath)
                for fname in os.listdir(targetPath):
                    fileDirectory = targetPath + fname
                    for fileType in file_name:
                            if fileType in fname:
                                #file directory is the full path
                                #CHECK THIS LATER
                                if(os.path.exists(fileDirectory)):                        
                                    #See if we can use targetPath instead
                                    # Split our path string based on the /'s 
                                    #This will assume that the path of an extracted flare follows the format: /Users/<user>/Downloads/<flare_name>
                                    splitPath = fileDirectory.split("/")

                                    #Drop the first and last entry
                                    slicedPath = splitPath[1:5]

                                    #Now we remake the path and remove the file
                                    pathToRemove = "/" + slicedPath[0] + "/" + slicedPath[1] + "/" + slicedPath[2] + "/" + slicedPath[3]
                                    shutil.rmtree(pathToRemove)
                                    print(f"{name} folder removed")

if __name__ == '__main__':
    removeExtractedFlares()