def get_parent_directory(path, levels):
    path_splits = path.split('\\')[:-levels]
    return_str = ''
    for element in path_splits:
        return_str += element + '\\'
    return return_str.rstrip('\\')
