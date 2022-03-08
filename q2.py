# Question 2
"""
# Write a program to scan the directory you are currently in and move the similar files to its respective folder

>> Image files in the docx folder
>> Pdf files in the pdf_folder
>> Text files in the txt_folder
>> Docx files in the docx_folder
>> Web files in the web_folder

# there are .py files in the folder, simply ignore them.
# when you organize your folder, only .py files should be in the main folder

How to write a program?

You need to create a two functions

organize() => move the files from the current folder to respective folder

disorganize() => move the files from the folder back to the main folder

Your program should run in the continous loop asking for user input.

If user enters 1 , your program should organize the files.
If user enters 2, your porgram should disorganize the files
If user enters 3, your program should stop

Please download the zip folder attached in the canvas. 

"""

import os
import shutil
from time import sleep


def organize():
    files_and_folders = os.listdir()
    files = [_ for _ in files_and_folders if os.path.isfile(_)]
    [shutil.move(_, 'image_folder') for _ in files if _.split('.')[1] == 'png']
    [shutil.move(_, 'docx_folder') for _ in files if _.split('.')[1] == 'docx']
    [shutil.move(_, 'txt_folder') for _ in files if _.split('.')[1] == 'txt']
    [shutil.move(_, 'web_folder') for _ in files if _.split('.')[1] == 'html']
    [shutil.move(_, 'pdf_folder') for _ in files if _.split('.')[1] == 'pdf']


def disorganize():
    current_dir = os.getcwd()
    files_and_folders = os.listdir()
    folders = [_ for _ in files_and_folders if (os.path.isdir(_) and _ != '.git')]
    for folder in folders:
        files_in_folder = [(f'{current_dir}{os.path.sep}{folder}{os.path.sep}' + _) for _ in os.listdir(folder)]
        if len(files_in_folder) != 0:
            [shutil.move(file, current_dir) for file in files_in_folder]


def program():
    while True:
        input_txt = '-------Program Start-------\nenter 1: To organize the files \nenter 2: To disorganize the ' \
                    'files\nenter 3: To quit\nEnter here: '
        user_input = input(input_txt)
        try:
            if user_input == '1':
                organize()
                print("RESULT:\nThe files are organized into respective directories\n")
            elif user_input == '2':
                disorganize()
                print("RESULT:\nAll files inside folders are placed back into main directory\n")
            elif user_input == '3':
                print("Thank you for using the program")
                sleep(1)
                break

        except Exception as e:
            print("Could not perform the task. The errors are: ")
            print(e)
            print("*** Please run the program in administrative mode in terminal ***\n")


if __name__ == "__main__":
    program()
else:
    program()
