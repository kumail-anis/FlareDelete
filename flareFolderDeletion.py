import os
from pathlib import Path

def main():
    #change path to Kumail's method

    # change path
    path = str(Path.home() / "Downloads/i-0f87e9dae64f7638b")
    file_name = ["status.log", "cluster-agent-status.log"]

    if not (path.endswith("/") or path.endswith("\\") ): 
        path = path + "/"

    if not os.path.exists(path):
        path =str(Path.home() / "Downloads")

    #fname is each filename within the folder (path)
    for fname in os.listdir(path):
        print(fname)
        fileDirectory = path + fname
        for fileType in file_name:
                if fileType in fname:
                    if(os.path.exists(fileDirectory)):                        
                        #back one repo
                        #delete path
                        print(fileDirectory +" found")   

if __name__ == '__main__':
    main()