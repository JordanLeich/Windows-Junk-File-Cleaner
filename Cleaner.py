# Made by Jordan Leich on 6/14/2020, Last updated on 7/13/2020 IMPORTANT NOTE TO READ*** This cleaner script will
# work best if you are an administrator on your PC. Without being an administrator, the script will only partially
# clean junk files and will eventually hit an error that will end the script.

# All imports used
import os
import shutil
import time
from colored import fg

# Extra global Variables used
good_color = fg('green')
bad_color = fg('red')
neutral = fg('blue')


# End of the program when the cleaner finishes cleaning junk files
def end():
    print(good_color + 'Cleaning successful!\n')
    time.sleep(1)
    quit()


# Second folder to clean (May require administrator)
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
            print(bad_color + 'Failed to delete %s. Reason: %s' % (file_path, e), '\n')
            third()


# Third folder to clean (Does require administrator)
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
            print(bad_color + 'Failed to delete %s. Reason: %s' % (file_path, e), '\n')
            time.sleep(1)
            end()


# Opens a cleaning program that is pre-installed with windows (Doesn't require administrator)
def first():
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    time.sleep(1)
    second()


# Beginning of the program
def start():
    user_choice = str(input(neutral + "Would you like to clean junk files on your computer (yes or no): "))

    if user_choice.lower() == 'yes' or user_choice.lower() == 'y':
        first()

    elif user_choice.lower() == 'no' or user_choice.lower() == 'n':
        print()
        print(good_color + "Ending cleaner...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input... Restart input...\n")
        time.sleep(2)
        start()


# Starts the first section of the program
start()
