import os

# Ask for the directory path from the user
directory = input("Enter the directory path (or leave blank for current directory): ")

# If the user entered nothing, use the current working directory
if directory == "":
    directory = "."

try:
    # Get list of files and directories
    contents = os.listdir(directory)
    
    # Print each item
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Error: You don't have