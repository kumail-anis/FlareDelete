import os

def main():
    #change path to Kumail's method
    path = "/Users/venus.parfait/Documents/test/notaflare.zip"
    zipFlareName = "datadog-agent"
    extension = ".zip"

    #check whether path exists and is a directory
    if os.path.exists(path):
        if os.path.isdir(path):
            #print("both all good")
            #to-do first call to walk to get info; print the first file

            # iterating through the subfolders
            for root, dirs, files in os.walk(path):
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
                            print("File is not a flare, do nothing")
        else:
            print(path, "is not a directory")
    else:
        print(path,"does not exist")
        #cannot use print(f"{path} blah blah")

if __name__ == '__main__':
    main()