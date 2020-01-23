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
    if len(sensitive_data_arr):
        dir = Path(os.path.abspath(__file__))
        fullpath = str(dir.parent)[:-11] + "/" + path
        print("Found sensitive data!")
        logging.warning(" Line: {} may contain sensitive data of type: {}.\n{}:{}\n".format(cnt, (", ").join(sensitive_data_arr), fullpath, cnt))


def is_sensitive(line_to_check):
    sensitive_data_regex_dictionary = _get_sensitive_data_dictionary()
    sensitive_data_detected = []
    for key in sensitive_data_regex_dictionary:
        if _is_sensitive_by_regex(sensitive_data_regex_dictionary[key], line_to_check, key):
            sensitive_data_detected.append(key)

    return sensitive_data_detected


def _get_sensitive_data_dictionary():
    logzio_shipping_token_regex = r"\b[a-zA-Z]{32}\b"
    logzio_api_token_regex = "([a-z]|[0-9]){8}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){11}"
    logzio_auth_token = r"\b(?:(?:us|ca|eu|ap){1}[-]{1}(?:east|central|southeast){1}[-]{1}[1-2]{1}|westeurope|westus2)[.]{1}[a-zA-Z]{32}\b"
    aws_access_key_regex = r"\b[A-Z0-9]{20}\b"
    regex_list = {"Logzio Shipping Token": logzio_shipping_token_regex}
    regex_list["Logzio Api Token"] = logzio_api_token_regex
    regex_list["Logzio Authentiation Token"] = logzio_auth_token
    regex_list["AWS Access Key"] = aws_access_key_regex
    return regex_list


def _is_sensitive_by_regex(regex, line_to_check, type_of_data):
    is_found_token = False
    match_obj = re.search(regex, line_to_check)
    if match_obj is not None and match_obj.group() is not None:
        if type_of_data in upper_and_lower_types:
            if _is_lower_and_upper_string(match_obj.group()):
                is_found_token = True
        else:
            is_found_token = True
    return is_found_token


def _is_lower_and_upper_string(lines):
    is_lower_and_upper = True
    for line in lines:
        if line.lower() == line and line.upper() == line:
            is_lower_and_upper = False
            break
    return is_lower_and_upper


walk_in_directory()