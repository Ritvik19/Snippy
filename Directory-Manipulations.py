import os, shutil

# Current working directory
os.getcwd()

# Change the CWD
os.chdir(PATH)

# Delete any directory
os.rmdir(PATH)

# Create a new directory
os.mkdir(PATH)

# Rename a directory
os.rename(OLD, NEW)

# Delete entire directory tree
shutil.rmtree(PATH)

# Copy entire directory tree
shutil.copytree(SRC, DST)

# Move file or directory
shutil.move(SRC, DST)
