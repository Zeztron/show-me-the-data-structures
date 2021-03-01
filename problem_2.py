import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    paths = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    else: 
        new_paths = os.listdir(path)
        for new_path in new_paths:
            paths += find_files(suffix, "{}/{}".format(path, new_path))            
    return paths

print(find_files('.c', 'testdir'))
print(find_files('.h', 'testdir'))
print(find_files('.c', '.'))
print(find_files('.c', 'testdir/subdir3/subsubdir1'))