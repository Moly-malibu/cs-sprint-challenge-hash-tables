"""
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]
 
queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
"""
from os import path
import os
# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    filenames = {}
    result = []

    for query in queries:
        filenames[query] = []
    for file in files:
        dictionary[file] = os.path.basename(file)
    for key in dictionary:
        if dictionary[key] in filenames:
            result.append(key)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
