# from pathlib import Path
# import os


# def create_folder():
#     try:
#         name = input("tell me your folder name")
#         p = Path(name)
#         p.mkdir()
#         print("your folder create successfully")
#     except Exception as err:
#         print(f"sorry error occured as {err}")


# def read_files_folder():
#     try:
#         p = Path("")
#         items = list(p.rglob('*'))
#         for i, v in enumerate(items):
#             print(f"{i+1} : {v}")
#     except Exception as err:
#         print(f"sorry error occured as {err}")


# def update_folder():
#     try:
#         read_files_folder()
#         old_name = input("please tell me which folder you want to update")
#         p = Path(old_name)
#         if p.exists() and p.is_dir():
#             new_name = input("please tell your new folder name")
#             new_p = Path(new_name) 
#             p.rename(new_p)
#             print("your folder name is updated successfully")
#         else:
#             print("sorry no such folder exist") 
#     except Exception as err:
#         print(f"an error occured as {err}") 


# def delete_folder():
#     try:
#         read_files_folder()
#         name = input("tell me which folder do you want to delete")
#         p = Path(name)
#         if p.exists() and p.is_dir():
#             p.rmdir()
#             print("folder delete successfully")
#         else:
#             print("no such folder exist")
#     except Exception as err:
#         print(f"an error occured as {err}")


# def create_file():
#     try:
#         read_files_folder()
#         name = input("tell me your file name")
#         p = Path(name)
#         if not p.exists():
#             with open (name,"w") as fs:
#                 data = input("write what you want in file ")
#                 fs.write(data)
#             print("file create successfully")
#         else:
#             print("sorry this file is already exist")
#     except Exception as err:
#         print(f"an error occures as {err}")  


# def read_file():
#     try:
#         read_files_folder()
#         name = input("tell me file name")
#         p = Path(name)
#         if p.exists() and p.is_file():
#             with open(name,'r') as fs:
#                 content = fs.read()
#                 print("yuor file content is")
#                 print(content)
#         else:
#             print("sorry no such file exist")
#     except Exception as err:
#         print(f"an error occured as {err}")


# def update_file():
#     try:
#         read_files_folder()
#         name = input("please tell your file name : ")
#         p = Path(name)
#         if p.exists() and p.is_file():
#             print("options ")
#             print("1. For renaming the file")
#             print("2. For appending something in the file ")
#             print("3. For overwriting the file content ")
#             choice = int(input("tell your choice : "))

#             if choice == 1:
#                 new_name = input("tell your new name with extension :- ")
#                 new_p = Path(new_name)
#                 if not new_p.exists():
#                     p.rename(new_p)
#                     print("your file nanme is changed successfully")
        
#                 else:
#                     print("sorry This name already exist")\
            
#             if choice == 2:
#                 with open(name,'a') as fs:
#                     data = input("what you want to append : ")
#                     fs.write(" "+ data)
#                 print("Data appended successfully ")

#             if choice == 3:
#                 with open(name,'w') as fs:
#                     data = input("what you want to overwrite : ")
#                     fs.write(data)
#                 print("Data changed successfully ")
#     except Exception as err:
#         print(f"An error occured as {err}")


# def delete_file():
#     try:
#         read_files_folder()
#         name = input("tell your file name with extension : ")
#         p = Path(name)
#         if p.exists() and p.is_file():
#             p.unlink()
#             print("file Deleted successfully")
#         else:
#             print("sorry no such file exist")
#     except Exception as err:
#         print(f"An error occured as {err}")

              
# print("options : ")
# print("1. created the folder")
# print("2. read the files and folder")
# print("3. update the folder")
# print("4. delete the folder")
# print("5. create a file")
# print("6. read a file")
# print("7. update a file")
# print("8. delete a file")



# choice = int(input("give me your choice"))


# if choice == 1:
#     create_folder()
# if choice == 2:
#     read_files_folder()
# if choice == 3:
#     update_folder()
# if choice == 4:
#     delete_folder()
# if choice == 5:
#     create_file()
# if choice == 6:
#     read_file()
# if choice == 7:
#     update_file()