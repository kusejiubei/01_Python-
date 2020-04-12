import os.path

root_dir = "D:\\data\\python"
list_dir = os.listdir(root_dir)
print("list_dir= ",list_dir)
for root, dirs, files in os.walk(root_dir):
    for dir_name in dirs:
        print("root is :", root)
        print("dir_name is :", dir_name)
    for file_name in files:
        print("root is : ", root)
        print("file_name is : ", file_name)
        print("the full name of the file is : ", os.path.join(root, file_name))
