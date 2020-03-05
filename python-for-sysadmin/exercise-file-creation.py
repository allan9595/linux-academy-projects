#!/usr/bin/env python3.6
'''
Ask filename
open the file and appaend line by line
if user does not type empty string, input will keep going
'''
fileName = input("Create a file name: ")
with open(fileName, 'a') as f:
    while True:
        content = input("Type something to the file: ")
        if content is not "":
            f.write(content + "\n")
        else:
            break

