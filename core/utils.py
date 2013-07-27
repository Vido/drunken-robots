import os


def get_relative_path(basefile, str_file):
    """ expected to be called: relative_path(__file__, db) """
    abspath = os.path.dirname(os.path.abspath(basefile))
    relpath = os.path.join(abspath, str_file)
    return relpath

