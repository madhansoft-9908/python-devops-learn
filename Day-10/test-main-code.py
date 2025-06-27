import os
def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None        # we are returning file and none-- output will be in tuple
    except FileNotFoundError:
        return None, "folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_path = input("Enter a list of folder paths separated by spaces: ").split()
    for folder in folder_path:
        files, error_message = list_files_in_folder(folder)   #this is called unpacking 
        #files gets the first item (the list of files)
        #error_message gets the second item (the error or None)
        print(files)    #output = ['containerd', 'python', 'dotnet', 'oryx', 'tmp', 'conda']
        #print(error_message)  = None

        #if we pass file = list_files_in_folder(folder) then oupt is tuple
        #output is tuple with two value list and string= (['containerd', 'python', 'dotnet', 'oryx', 'tmp', 'conda'], None)
        for file in files:
            print(file)
#final output=
#containerd
#python
#dotnet
#oryx
#tmp
#conda


if __name__ == "__main__":
    main()
