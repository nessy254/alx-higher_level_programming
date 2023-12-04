#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for str in range(len(my_string)):
        if my_string[str] != "c" and my_string[str] != "C":
            new_str += my_string[str]
    return new_str
