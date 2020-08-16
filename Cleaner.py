# Made by Jordan Leich on 6/14/2020, Last updated on 8/15/2020 IMPORTANT NOTE TO READ*** This cleaner script will
# work best if you are an administrator on your PC. Without being an administrator, the script will only partially
# clean junk files and will eventually hit an error that will end the script.

# All imports used
import os
import shutil
import time as ti
from colored import fg, attr

# Extra global Variables used
green = fg('green')
red = fg('red')
reset_color = attr('reset')


def end():
    """
    End of the program when the cleaner finishes cleaning junk files
    """
    print(green + 'Cleaning Successful!\n', reset_color)
    ti.sleep(1)
    quit()


def second():
    """
    Second folder to clean (May require administrator)
    """
    folder = 'C:\Windows\Temp'
    ti.sleep(1)
    list = os.listdir(folder)
    number_files = len(list)
    print(red + 'Junk files/folders found in the first folder: ', number_files, reset_color, '\n')
    ti.sleep(2)

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        print(green + "Deleted " + filename, '\n', reset_color)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(red + 'Failed to delete %s. Reason: %s' % (file_path, e), '\n', reset_color)
            ti.sleep(1)
            third()


def third():
    """
    Third folder to clean (Does require administrator)
    """
    second_folder = 'C:\Windows\Prefetch'
    ti.sleep(1)
    list = os.listdir(second_folder)
    number_files = len(list)
    print(red + 'Junk files/folders found in the second folder: ', number_files, reset_color, '\n')
    ti.sleep(2)

    for filename in os.listdir(second_folder):
        file_path = os.path.join(second_folder, filename)
        print(green + "Deleted " + filename, '\n', reset_color)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(red + 'Failed to delete %s. Reason: %s' % (file_path, e), '\n', reset_color)
            ti.sleep(1)
            end()


def first():
    """
    Opens a cleaning program that is pre-installed with windows (Doesn't require administrator)
    """
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    ti.sleep(1)
    second()


def basic_clean():
    """
    Basic Clean - Opens a cleaning program that is pre-installed with windows (Doesn't require administrator)
    """
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    ti.sleep(1)
    end()


def start():
    """
    This is the very start of the program, the user is asked for input to choose between a basic or advanced
    cleaning, or they can choose to quit the program.
    """
    try:
        user_choice2 = str(input('Basic clean, Advanced clean, or quit (basic, advanced, or quit): '))
        print()

        if user_choice2.lower() == 'basic' or user_choice2.lower() == 'b':
            print('Basic clean running...', reset_color)
            basic_clean()

        elif user_choice2.lower() == 'advanced' or user_choice2.lower() == 'a':
            print('Advanced clean running...', reset_color)
            first()

        elif user_choice2.lower() == 'quit' or user_choice2.lower() == 'q':
            print('Ending cleaner...')
            ti.sleep(1)
            quit()

        else:
            print(red + "Invalid input... Restart input...\n", reset_color)
            ti.sleep(1)
            start()

    except Exception as e:
        print(red, e, '\n', reset_color)
        ti.sleep(3)
        quit()


start()  # Starts the first section of the program
