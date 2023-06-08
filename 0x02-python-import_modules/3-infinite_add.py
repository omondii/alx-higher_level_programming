#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arguments_list = sys.argv[1:]
    for argument in arguments_list:
        sum += int(argument)
    print("{}".format(sum))
