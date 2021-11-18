import os

def main():
    path = '/Users/venus.parfait/Downloads/sec-iam-clm-prd-ff2f-west-vm2_us/'
    name = 'datadog-agent-'

    #check whether path exists and is a directory
    if os.path.exists(path):
        if os.path.isdir(path):
            print("both all good")

            # iterating through the subfolders
            #this doesn't work for downloads
            for root, dirs, files in os.walk(path):
                for name in files:
                    print(os.path.join(root, name))

        else:
            print(f"{path} is not a directory")
    else:
        print(f"{path} does not exist")

if __name__ == '__main__':
    main()