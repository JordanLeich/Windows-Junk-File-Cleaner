# Made by Jordan Leich on 6/14/2020

import os
import shutil
import time


def first():
    folder = 'C:\Windows\Temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            second()


def second():
    folder = 'C:\Windows\Prefetch'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            third()


def third():
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    quit()


def start():
    user_choice = str(input("Would you like to clean junk files on your computer (yes | no): "))
    print()

    if user_choice.lower() == 'yes' or user_choice.lower() == 'y':
        first()

    else:
        print("Ending cleaner...")
        print()
        time.sleep(2)
        quit()


start()
