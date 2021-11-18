import os

def main():
    path = '/Users/venus.parfait/Downloads'
    name = 'datadog-agent-'

    #check whether path exists and is a directory
    if os.path.exists(path):
        if os.path.isdir(path):
            print("both all good")
        else:
            print("not valid")

if __name__ == '__main__':
    main()