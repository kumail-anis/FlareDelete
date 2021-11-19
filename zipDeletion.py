import os
from pathlib import Path
import shutil

def zipDeletion():
    #This will delete any .zip files in your downloads folder where datadog-agent is part of the path
    zipFlareName = "datadog-agent"
    extension = [".zip", ".ZIP", ".gz"]
    search_path = str(Path.home() / "Downloads")

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
                    for fileExtension in extension:
                    #Check if the file_extension is a zip
                        if fileExtension == file_extension:
                            #Check that the file_path contains zipFlareName - could improve
                            if zipFlareName in file_path:
                            # Delete the file
                                if not os.remove(file_path):
                                    # success message
                                    print(f'{name} File deleted successfully')
                                    
                                else:
                                    # failure message - possibly permissions issue
                                    print("Unable to delete the file")

        else:
            print("f{search_path} is not a directory")
    else:
        print(f"{search_path} does not exist")

if __name__ == '__main__':
    zipDeletion()