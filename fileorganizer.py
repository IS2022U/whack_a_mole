# #import os

# # #getcwd-- get current working directory
# # #print(os.getcwd())
# # #chdir-- change directory
# # #os.chdirr("\Users\ishus\OneDrive\Desktop\day 1")
# # #os.mkdir("today")
# # #print(os.listdir())

# # from pathlib import Path
# # #split()--splits the file path it needs path library
# # # x,y=os.path.splitext("demo.png")
# # # print(x)
# # # #print(y)
# import os
# from pathlib import Path
# import shutil
# # #shutil --moves
# os.chdir(r"C:\Users\ishus\OneDrive\Desktop\day 1")

# manager={
#     "images":[".png",".jpg",".jpeg"],
#     "Document":[".pdf",".exe",".docx"],
#     "script":[".py",".html"]
#     }

# # for folder in manager:
# #     os.makedirs(folder,exist_ok=True)
    
# # for get_file in os.listdir():
# #     file_ext=get_extension(get_file)
    
# #     for folder in manager:
# #         os.makedirs()
# for folder in manager:
#     os.makedirs(folder,exist_ok= True )

# def get_extension(file_name):
#     return os.path.splitext(file_name)[1] #return second index of tuple

# #exception = for current .py file

# for get_file in os.listdir():
#     file_ext=get_extension(get_file)
#     for folder_name,extension_list in manager.items():
#         if file_ext in extension_list:
#             shutil.move(get_file,folder_name)
# #print(os.listdir)
