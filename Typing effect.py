import time

string = i for i in input('Copy Paste your string: ')
str(string)

def message(string):
    for i in string:
        print(i, end="")
        time.sleep(0.5)

message(string)