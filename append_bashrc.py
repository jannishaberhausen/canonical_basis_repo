import os


def read_bashrc_appendix(filepath=None):
    if filepath is None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, '.bashrc_appendix')
    appendix = []
    with open(file_path) as f:
        for line in f:
            appendix.append(line)
    return appendix
            

def append_bashrc(appendix, bashrc_path=None):
    if bashrc_path is None:
        bashrc_path = os.path.expanduser('~/.bashrc')
    with open(bashrc_path, 'a') as f:
        for line in appendix:
            f.write(line)
        
def main():
    appendix = read_bashrc_appendix()
    append_bashrc(appendix)


if __name__ == '__main__':
    main()
    