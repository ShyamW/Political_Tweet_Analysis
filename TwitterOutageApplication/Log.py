"""Log Module that logs everything the program does.
@author Shyam Thiagarjan
"""


"""Prints information into text file and to console window.
@param text
    String to be recorded"""
def record(text):
    print(text)
    out = open('log.txt', 'a')
    out.write(text + '\n')
    out.close()
