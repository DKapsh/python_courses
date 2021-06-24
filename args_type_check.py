import sys

def is_int(val):
    try:
        int(val)
    except ValueError:
        return False
    return True
    

def is_float(val):
    try:
        float(val)
    except ValueError:
        return False
    return True

def print_args_list(title, items):
    if (items):
        print(title)
        for item in items:
            print(item)

def find_substring(substr, strings):
    result = []
    for string in strings:
        if substr in string:
            result.append(string)
    return result

def main():

    if (len(sys.argv) == 1):
        print("No arguments")
        return

    integers = []
    floats = []
    strings = []

    for arg in sys.argv[1:]:
        if (is_int(arg)):
            integers.append(arg)
        elif (is_float(arg)):
            floats.append(arg)
        else:
            strings.append(arg)

    print_args_list("Integers:", integers)
    print_args_list("Strings:", strings)
    print_args_list("Floats:", floats)

    last_arg = sys.argv[-1]
    strings_with_substrings = []
    if (not is_int(last_arg)) and (not is_float(last_arg)):
        strings_with_substrings = find_substring(last_arg, sys.argv[:-1])
        title = "Found string '" + last_arg + "' in following args:"
        print_args_list(title, strings_with_substrings)

main()


