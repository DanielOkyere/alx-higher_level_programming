#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """Writes a sting to text file and returns the numbe of characters
    writen
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
