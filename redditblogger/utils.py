import os, errno

def mkdir_p(path):
    # os.makedirs(folder, exist_ok=True) # Python 3
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
