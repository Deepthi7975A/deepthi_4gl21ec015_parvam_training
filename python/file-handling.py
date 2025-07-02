# creating a file using open method with 'x' mode, if the file already exists it throws an  error # create- x
# with open("new_file.txt", "x") as f:
#     f.write("Newly created the text file using python with 'x' mode.") 

# overwrite the file if it already exists without any error, if not them crete a new file
with open("new_file.txt", "w") as f:
    f.write(" the text file creted using python with 'w' mode.")

# overwrite the file or update if it already exixts without any error, if not them crete a new file
with open("new_file.txt", "a") as f:
    f.write(" \n The new text has been added or appended using 'a' mode")

#writing the content to a file
with open("new_file.txt", "w") as f:
    f.write("This is first sentence.\n")
    f.write("This is second sentence.")

#Redding the content from a file
with open("new_file.txt", "r") as f:
    for line in f :
        print(line.strip())
print(type(line.strip()))


#Redding the content from a file and make it as a list using readlines method
with open("new_file.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))

#Redding the content from a file using readline method for only first line
with open("new_file.txt", "r") as f:
    lines = f.readline()
    print(line)
    print(type(line))

#renaming a file
# import os
# os.rename("new_file.txt", "sample_file.txt")
# print("File renamed from new_file.txt to sample_file_txt")

#check whether the file is opened or closed
file = open("sample_file.txt", "r")
print("File is closed?", file.closed)
file.close()
print("File is closed?", file.closed)

#deleting a file
import os
if os.path.exists("sample_file.txt"):
    os.remove("sample_file.txt")
    print("The file has been deleted!")
else:
    print("The file has not been deleted!")

