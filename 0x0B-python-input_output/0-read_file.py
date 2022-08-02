#!/usr/bin/python3
"""Defines a file for Reading files"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
