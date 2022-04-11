__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from os import listdir
import shutil
from zipfile import ZipFile
import re

dir = os.path.join(os.getcwd(), 'files')

def clean_cache():
    dirname = 'cache'
    path = os.path.join(dir, dirname)
    if not os.path.exists(path):
        os.mkdir(path)
    else: 
        shutil.rmtree(path)
        os.mkdir(path)

def cache_zip(file_path, dir_path):
    with ZipFile(file_path, 'r') as zipObj:
        zipObj.extractall(dir_path)

def cached_files():
    abs_files = []
    new_dir = os.path.join(dir, 'cache')
    for file in os.listdir(new_dir):
        path = os.path.join(new_dir, file)
        if os.path.isfile(path):
                abs_files.append(path)
    return abs_files

def find_password(list_files):
    for file in list_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    password = line.removeprefix('password: ')
                    return password[:-1]