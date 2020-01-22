import os
import sys
import re
import logging
from pathlib import Path

upper_and_lower_types = {"logzio shipping token"}
rootpath_arr = sys.argv[1:len(sys.argv)]


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
                search_regex(file_path, line, cnt)
                line = fp.readline()
                cnt += 1
    except:
        pass


def search_regex(path, line, cnt):
    sensitive_data_arr = is_sensitive(line)
    for sensitive_data in sensitive_data_arr:
        dir = Path(os.path.abspath(__file__))
        fullpath = str(dir.parent)[:-11] + "/" + path
        logging.error("Warning! Line: {} may contain sensitive data:\n{}:{}\n{}\n".format(cnt, fullpath, cnt, sensitive_data.strip()))
        print("Found sensitive data\n")


def is_sensitive(line_to_check):
    sensitive_data_regex_dictionary = _get_sensitive_data_dictionary()
    sensitive_data_detected = []
    for key in sensitive_data_regex_dictionary:
        if _is_sensitive_by_regex(sensitive_data_regex_dictionary[key], line_to_check, key):
            sensitive_data_detected.append(key)
    return sensitive_data_detected


def _get_sensitive_data_dictionary():
    logzio_shipping_token_regex = "([a-zA-Z]{32})"
    regex_list = {"logzio shipping token": logzio_shipping_token_regex}
    return regex_list


def _is_sensitive_by_regex(regex, line_to_check, type_of_data):
    is_found_token = False
    match_obj = re.search(regex, line_to_check)
    if match_obj is not None:
        if match_obj.start() == 0 and match_obj.end() == len(line_to_check):
            is_found_token = True
        else:
            before_index = match_obj.start() - 1
            after_index = match_obj.end()
            if match_obj.start() == 0:
                if (not line_to_check[after_index].islower()) and (not line_to_check[after_index].isupper()):
                    is_found_token = True
            if match_obj.end() == len(line_to_check):
                if (not line_to_check[before_index].islower()) and (not line_to_check[before_index].isupper()):
                    is_found_token = True
            else:
                if (not line_to_check[before_index].islower()) and (not line_to_check[before_index].isupper()) and\
                        (not line_to_check[after_index].islower()) and (not line_to_check[after_index].isupper()):
                    is_found_token = True
        if is_found_token and type_of_data in upper_and_lower_types:
            if not _is_lower_and_upper_string(match_obj.group()):
                is_found_token = False
    return is_found_token


def _is_lower_and_upper_string(lines):
    is_lower_and_upper = True
    for line in lines:
        if line.lower() == line and line.upper() == line:
            is_lower_and_upper = False
            break
    return is_lower_and_upper


walk_in_directory()
