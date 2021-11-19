import fileSearch
import zipDeletion
import extractedFlareDeletion

def main():
    try:
        zipDeletion.zipDeletion()
        extractedFlareDeletion.removeExtractedFlares()
        fileSearch.fileSearchPath()
    except SyntaxError:
        print("file was not found")

if __name__ == '__main__':
    main()