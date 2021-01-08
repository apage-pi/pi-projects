# Python program to explain shutil.copyfile() method

#This is a note: create the file test.txt in the source file in repl and if on RPi, modify the user, create the folders, and create test.txt

# importing shutil module
import shutil

# Source path
source = "/home/runner/source/test.txt"

# Destination path
destination = "/home/runner/dest/textsucsess.txt"

# Copy the content of
# source to destination

try:
    shutil.copyfile(source, destination)
    print("File copied successfully.")

# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")

# If destination is a directory.
except IsADirectoryError:
    print("Destination is a directory.")

# If there is any permission issue
except PermissionError:
    print("Permission denied.")

# For other errors
except:
    print("Error occurred while copying file.")
