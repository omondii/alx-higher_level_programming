#!/usr/bin/python3
"""
No modules imported
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text after each line containing a specific
    string in a file.
    Params:
        filename: Name of the file to modify.
        search_string: String to search for in each line.
        new_string: Line of text to insert after each line containing the
                    search string.
    """
    with open(filename, "r") as input_file:
        """
        Open the input file in read mode.
        Read the file line by line
        """
        lines = input_file.readlines()

    with open(filename, "w") as output_file:
        """
        open the output file inwrite mode
        loop over each linein the file, write the original line to the
        output file.
        Check if the search string exists in the line. If it exixts:
        insert the new string after the line
        """
        for line in lines:
            output_file.write(line)
            if search_string in line:
                output_file.write(new_string)
