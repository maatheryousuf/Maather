MEMORY = 20
FILE_SIZE = 12
numberof_files = int(input("Enter the number : "))

if (numberof_files * FILE_SIZE <= MEMORY):
    print("You can store the files")

else:
    print("You cannot store the files, there is no space")
