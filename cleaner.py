# Made by Jordan Leich on 6/14/2020, IMPORTANT NOTE TO READ*** This cleaner script will
# work best if you are an administrator on your PC. Without being an administrator, the script will only partially
# clean junk files and will eventually hit an error that will end the script.

# All imports used
import os
import shutil
from time import sleep
from colored import fg, attr

green = fg('green')
red = fg('red')
yellow = fg('yellow')
reset_color = attr('reset')


def end():
    """
End of the program when the cleaner finishes cleaning all junk files
    """
    print(green + 'Cleaning Successful!\n', reset_color)
    sleep(1)
    quit()


def first_folder_cleaner():
    """
Second folder to clean (May require administrator)
    """
    folder = 'C:\Windows\Temp'
    sleep(1)
    directory_list = os.listdir(folder)
    number_files = len(directory_list)
    print(red + 'Junk files/folders found in the first folder:', number_files, reset_color, '\n')
    sleep(2)

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
            sleep(1)
            second_folder_clean()


def second_folder_clean():
    """
Third folder to clean (Does require administrator)
    """
    second_folder = 'C:\Windows\Prefetch'
    sleep(1)
    directory_list = os.listdir(second_folder)
    number_files = len(directory_list)
    print(red + 'Junk files/folders found in the second folder:', number_files, reset_color, '\n')
    sleep(2)

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
            sleep(1)
            end()


def first_cleaner():
    """
Opens a cleaning program that is pre-installed with windows (Doesn't require administrator) and then proceeds to clean
other folders
    """
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    sleep(1)
    first_folder_cleaner()


def basic_clean():
    """
Opens a cleaning program that is pre-installed with windows (Doesn't require administrator) and then quits the program
    """
    clean = os.popen('cleanmgr.exe /sagerun:1').read()
    print(clean)
    sleep(1)
    end()


def main():
    """
This is the very start of the program, the user is asked for input to choose between a basic or advanced
cleaning, or they can choose to quit the program
    """
    try:
        user_choice2 = str(input('Basic clean, Advanced clean, or quit (basic, advanced, or quit): '))
        print()

        if user_choice2.lower() in ['basic', 'b']:
            print('Basic clean running...', reset_color)
            basic_clean()

        elif user_choice2.lower() in ['advanced', 'a']:
            print('Advanced clean running...', reset_color)
            first_cleaner()

        elif user_choice2.lower() in ['quit', 'q']:
            print('Ending cleaner...')
            sleep(1)
            quit()

        else:
            print(red + "Invalid input... Restart input...\n", reset_color)
            sleep(1)
            main()

    except Exception as e:
        print(red, e, '\n', reset_color)
        sleep(2)
        quit()


main()  # Starts the first section of the program

if __name__ == '__main__':
    main()
