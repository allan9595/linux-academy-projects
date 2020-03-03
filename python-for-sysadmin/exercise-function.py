#!/usr/bin/env python3.6

message = input("Enter a message: ")
count = input("Number of times to repeat the message: ") or 1

#print the message out
def display(message, count):
    if not message:
         print('No message has been entered!')
    else:
        i = 0
        while i < int(count):
            print(message)
            i = i + 1

display(message,count)

