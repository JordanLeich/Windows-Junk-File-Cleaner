# Made by Jordan Leich on 6/14/2020

import os
import shutil
import time


def end():
    print()
    print('Cleaning successful!\n')
    time.sleep(2)
    quit()


def second():
    folder = 'C:\Windows\Temp'
    time.sleep(2)
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
    folder = 'C:\Windows\Prefetch'
    time.sleep(2)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            end()


def first():
    time.sleep(2)
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    time.sleep(1)
    second()


def start():
    user_choice = str(input("Would you like to clean junk files on your computer (yes or no): "))
    print()

    if user_choice.lower() == 'yes' or user_choice.lower() == 'y':
        first()

    elif user_choice.lower() == 'no' or user_choice.lower() == 'n':
        print("Ending cleaner...")
        time.sleep(2)

    else:
        print("Invalid input... Restart input...\n")
        time.sleep(2)
        start()


start()
