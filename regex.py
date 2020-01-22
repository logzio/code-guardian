import re


def is_sensitive(line_to_check):
    sensitive_data_regex_dictionary = _get_sensitive_data_dictionary()
    sensitive_data_detected = []
    for key in sensitive_data_regex_dictionary:
        if _is_sensitive_by_regex(sensitive_data_regex_dictionary[key], line_to_check):
            sensitive_data_detected.append(key)

    return sensitive_data_detected


def _get_sensitive_data_dictionary():
    logzio_shipping_token_regex = "([a-zA-Z]{32})"
    regex_list = {"logzio shipping token": logzio_shipping_token_regex}
    return regex_list


def _is_sensitive_by_regex(regex, line_to_check):
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
    return is_found_token
