import os
import shutil


# Current directory is a directory where a cookiecutter template was rendered
current_directory = os.getcwd()

# Parent directory is a directory where we have called the cookiecutter cmd
parent_directory = os.path.dirname(current_directory)

# copytree copies all the contents from current and all nested directories
# from source folder to a destination folder.
shutil.copytree(current_directory, parent_directory, dirs_exist_ok=True)
