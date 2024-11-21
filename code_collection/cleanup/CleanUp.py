import os

#homeDir="C:/practice" #where the files are in the directory,

# files must be placed in e.g. "C:/practice/sample"
workDir = os.getcwd()
homeDir = os.path.join(workDir, "sample") # where the files are
print("Working directory:", workDir)
print("Home directory:", homeDir)
print()

totalSize= 0
numberTextFile = 0
print("List of text files:")
for txtFile in os.listdir(homeDir): #accessing the files from the folder.

    fileName, fileExtension = os.path.splitext(txtFile)
    if fileExtension == ".txt": #everything text file related
        logFileLocation = os.path.join(homeDir, txtFile) #getting the full path of the text file
        fileSize = os.path.getsize(logFileLocation) #getting the file size
        totalSize = totalSize + fileSize #adding up every file size
        numberTextFile = numberTextFile + 1
        print(logFileLocation, "=" , fileSize ,"bytes")

averageSize = int(totalSize / numberTextFile) #finding the average of the file
print("Total file size: ",  totalSize ,"bytes")
print()
print("Total number of text files:" ,numberTextFile)
print()
print("Average size of all text files:" ,averageSize ,"bytes")
print()

print("List of non-text files")
for txtFile in os.listdir(homeDir): #accessing the files from the folder.

    fileName, fileExtension = os.path.splitext(txtFile)
    if fileExtension != ".txt": #not txt file
        logFileLocation = os.path.join(homeDir, txtFile)  # getting the full path of the text file

        print(logFileLocation,)