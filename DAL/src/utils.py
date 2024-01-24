import os

def get_parent_directory(path, levels):
    list = path.split('\\')[:-levels]
    return_str = ''
    for element in list:
        return_str += element + '\\'
    return return_str.rstrip('\\')
