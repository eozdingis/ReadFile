import os

def readFiles (folderPath):
    dirList = os.listdir(folderPath)
    return dirList

def main():
    pdfFolderPath = os.path.normpath("D:\Can Bakiler Production")
    pdfFileList = readFiles(pdfFolderPath)
    print(pdfFileList)

if __name__ == '__main__':
    main()
