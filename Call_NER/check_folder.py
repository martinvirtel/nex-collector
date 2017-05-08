import os
import os.path
import errno


def check_folder (filepath): 
    try: 
        os.makedirs(filepath)
    except OSError:
        if not os.path.isdir(filepath):
            raise