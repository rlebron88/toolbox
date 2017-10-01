
import os
import mimetypes

__author__ = 'antonior'


def make_dir(path):
    'It creates a directory if it does not exist'
    if not os.path.exists(path):
        os.makedirs(path)
    return


def istext(filename):
    mime = mimetypes.guess_type(filename)[0]
    if mime is None or 'text' in mime:
        return True
    return False

def istabfile(filename):
    with open(filename) as fd:
        if len(fd.readline().split("\t")) > 1:
            return True
        else:
            return False
