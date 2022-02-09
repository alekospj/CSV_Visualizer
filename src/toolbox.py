import os

def create_full_dir(DIRECTORY):
    new_dir = DIRECTORY
    cwd = os.getcwd()

    dir_split = new_dir.split('/')
    new_total = cwd

    for ele in dir_split:

        '''Checking if not exist a directory'''
        new_total = new_total + '/' + ele + '/'

        try:
            os.stat(new_total)
        except:
            os.mkdir(new_total)

    return DIRECTORY