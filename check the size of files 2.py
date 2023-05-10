memory = int(input("Enter the size of Memory : "))
file_size = int(input("Enter the file size : "))
numberof_files = int(input("Enter the number : "))

if (numberof_files * file_size <= memory):
    print("You can store the files")

else:
    print("You cannot store the files, there is no space")
