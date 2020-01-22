import os
import sys

rootpath_arr = sys.argv[1:len(sys.argv)]
regex = "script"


def walk_in_directory():
    for rootpath in rootpath_arr:
        if os.path.isdir(rootpath):
            for subdir, dirs, files in os.walk(rootpath):
                for file in files:
                    filepath = subdir + os.sep + file
                    check_file_data(filepath)
        elif os.path.isfile(rootpath):
            check_file_data(rootpath)


def check_file_data(file_path):
    try:
        with open(file_path) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                find_regex_mock(file_path, line, cnt)
                line = fp.readline()
                cnt += 1
    except:
        pass


def find_regex_mock(path, line, cnt):
    if line.find(regex):
        print("Warning! Line: {} may contain sensitive data:\n{}:{}\n{}\n".format(cnt, path, cnt, line.strip()))


walk_in_directory()
