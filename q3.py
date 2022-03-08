# 3
# Question 3

"""
Write a porgram to transverse the folder you are in and list the folder and the files recursively. 
For example, if you run your code in the folder given above, when the files are organized your program should
print all the files and folders inside that folder. 
"""
import os
from time import sleep

total_exceptions = []


def explore(path):
    path = os.path.abspath(path)
    try:
        folders = [path + os.path.sep + i for i in os.listdir(path) if os.path.isdir(path + os.path.sep + i)]
        files = [path + os.path.sep + i for i in os.listdir(path) if os.path.isfile(path + os.path.sep + i)]

        if files is not None:
            for file in files:
                print(" " * file.count(os.path.sep) + file)

        if len(folders) != 0:
            for folder in folders:
                print(" " * folder.count(os.path.sep) + folder)
                explore(folder)
                sleep(0.08)
    except Exception as e:
        total_exceptions.append(e)

    # 1. identify whether it is a folder or file
    # 2. if its a folder, you want to go inside that folder and then look for more folder


path = ""
explore(path)

if __name__ == '__main__':
    path = ""
    explore(path)

    if len(total_exceptions) != 0:
        print("Errors: ", total_exceptions)

"""
The display order of the files/folder dont matter
"""
