import os

current_dir = os.getcwd()

print(f"You are currently in {current_dir}")




while True:
    try:
        print("Create your own directory..")
        print("Give name for the directory.....")

        name_of_dir = input()

        os.mkdir(name_of_dir)
        bool=True
        break
    except Exception as e:
        print("Either directory is already there or invalid directory file")
        bool = False
        print("Try Again")

if bool==True:
    print("Directory Succesfully Created")















