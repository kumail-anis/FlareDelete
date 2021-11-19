import os
from pathlib import Path

def main():
    #main will delete any .zip files in your downloads folder where datadog-agent is part of the path
    #old method
    #path = "/Users/venus.parfait/Documents/test/notaflare.zip"
    zipFlareName = "datadog-agent"
    extension = ".zip"
    #get home directory
    home_dir = str(Path.home())
    search_path = str(Path.home() / "Documents/test/")

    #testing
    print(home_dir)
    removeExtractedFlares()

    #check whether path exists and is a directory
    if os.path.exists(search_path):
        if os.path.isdir(search_path):
            #print("both all good")
            #to-do first call to walk to get info; print the first file

            # iterating through the subfolders
            for root, dirs, files in os.walk(search_path):
                for name in files:
                    # get the file path
                    file_path = os.path.join(root, name)

                    # extract the extension from the filename
                    file_extension = os.path.splitext(file_path)[1]

                    # checking the file_extension
                    if extension == file_extension:
                        #for each zip file check that the file_path contains zipFlareName - could make more specific?? 
                        if zipFlareName in file_path:
                        # Delete the file
                            if not os.remove(file_path):
                                # success message
                                print("File deleted successfully")
                                
                            else:
                                # failure message
                                print("Unable to delete the file")
                        else:
                            print("File is not a flare")
        else:
            print(f"{search_path} is not a directory")
    else:
        print(f"{search_path} does not exist")

def removeExtractedFlares():
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
        


if __name__ == '__main__':
    main()
