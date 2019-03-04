import os

def  print_directory_contents(sPath):
    """
        This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk

    :param sPath: string with valid directory path
    :return: Generator of files in directory, and files in subdirectories
    """
    for file in os.listdir(sPath):
        if os.path.isdir(os.path.join(sPath, file)):
            for subfile in print_directory_contents(os.path.join(sPath, file)):
                yield os.path.join(file, subfile)
        else:
            yield(file)

