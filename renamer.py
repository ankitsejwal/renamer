import os
import sys
import re

def rename(directory_path, string):
    os.chdir(directory_path)
    print('The file(s) will look like this after renaming:')
    for fil in os.listdir(directory_path):
        print(re.sub(string, '', fil))
    
    ans = ''
    while ans.lower() != 'y' or ans.lower() != 'n':

        ans = input('\nDo you wish to continue? (Y/N): ')
        if ans.lower() == 'y':
            for fil in os.listdir(directory_path):
                new_name = re.sub(string, '', fil)
                os.rename(fil, new_name)
            print('-> All files renamed successfully.')
            return
        elif ans.lower() == 'n':
            print('-> Alright, You choose not to rename the files!\n')
            return
        else:
            print('-> OOPS, press either Y or N')

if __name__ == '__main__':
    rename('/Users/ankitsejwal/Desktop/Flask-tutorial','Flask Tutorial Web Development with Python ')
