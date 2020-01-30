import re
import string


def contains_regex(regex, line_to_check):
    is_sensitive = False
    match_obj = re.search(regex, line_to_check)
    if match_obj is not None and match_obj.group() is not None:
        is_sensitive = True
    return is_sensitive


def contains_lower_and_upper(exp):
    return contains_lower(exp) and contains_upper(exp)


def contains_lower(exp):
    return any(char.islower() for char in exp)


def contains_upper(exp):
    return any(char.isupper() for char in exp)


def contains_digit(exp):
    return any(char.isdigit() for char in exp)


def contains_special_char(exp):
    invalid_chars = string.punctuation
    return any(char in invalid_chars for char in exp)