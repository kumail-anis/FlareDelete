import os

def main():
    path = "/Users/venus.parfait/Downloads"
    name = "datadog-agent-"
    extension = ".zip"

    #check whether path exists and is a directory
    if os.path.exists(path):
        if os.path.isdir(path):
            print("both all good")

            #to-do first call to walk to get info; print the first file

            # iterating through the subfolders
            for root, dirs, files in os.walk(path):
                for name in files:
                    # file path
                    file_path = os.path.join(root, name)

                    # extracting the extension from the filename
                    file_extension = os.path.splitext(file_path)[1]


                    # checking the file_extension
                    if extension == file_extension:
                        # deleting the file
                        if not os.remove(file_path):
                            # success message
                            print("file deleted successfully")
                            
                        else:
                            # failure message
                            print("Unable to delete the file")
        else:
            print("is not a directory")
    else:
        print("does not exist")

if __name__ == '__main__':
    main()