import os
import sys
import logging
import utils


logzio_shipping_token_regex = r"\b[a-zA-Z]{32}\b"
logzio_api_token_regex = "([a-z]|[0-9]){8}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){4}[-]{1}([a-z]|[0-9]){11}"
logzio_auth_token = r"\b(?:(?:us|ca|eu|ap){1}[-]{1}(?:east|central|southeast){1}[-]{1}[1-2]{1}|westeurope|westus2)[.]{1}[a-zA-Z]{32}\b"
aws_access_key_regex = r"\b[A-Z0-9]{20}\b"
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
            line_index = 1
            while line:
                check_sensitive(file_path, line, line_index)
                line = fp.readline()
                line_index += 1
    except:
        logging.error("Could not read file: {}".format(file_path))
        pass


def check_sensitive(path, line, line_index):
    sensitive_data_arr = is_sensitive(line)
    if len(sensitive_data_arr):
        logging.warning(" Line: {} may contain sensitive data of type: {}.\n{}:{}\n".format(line_index, (", ").join(sensitive_data_arr), path, line_index))
        print("Found sensitive data!")


def is_sensitive(line):
    sensitive_data_detected = []
    for data_type in functions_map:
        func_is_sensitive = functions_map[data_type]
        if func_is_sensitive(line):
            sensitive_data_detected.append(data_type)
    return sensitive_data_detected


def contains_logzio_shipping_token(line):
    if not utils.contains_regex(logzio_shipping_token_regex, line):
        return False
    if not utils.contains_lower_and_upper(line):
        return False
    return True


def contains_logzio_api_token(line):
    if not utils.contains_regex(logzio_api_token_regex, line):
        return False
    return True


def contains_logzio_authentication_token(line):
    if not utils.contains_regex(logzio_auth_token, line):
        return False
    exp = line.split('.')[1]
    if not utils.contains_regex(logzio_shipping_token_regex, exp):
        return False
    if not utils.contains_lower_and_upper(exp):
        return False
    return True


def contains_aws_access_key(line):
    if not utils.contains_regex(aws_access_key_regex, line):
        return False
    return True


functions_map = {
     "Logzio Shipping Token": contains_logzio_shipping_token,
     "Logzio API Token": contains_logzio_api_token,
     "Logzio Authentiation Token": contains_logzio_authentication_token,
     "AWS Access Key": contains_aws_access_key
}

walk_in_directory()