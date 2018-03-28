#!/bin/python

import sys

this = []

def isEmpty():
    global this
    return this == []

def push(item):
    global this
    this.append(item)

def pop():
    global this
    return this.pop()

def size():
    global this
    return len(this)


print "Input digit: "
d = int(input())
if d == 0:
    print "Binary digit is: 0"
else:
    while d:
        push(d % 2)
        d /= 2

    print "Binary digit is: "
    while isEmpty() == False:
        sys.stdout.write(str(pop()))
    sys.stdout.write("\n")
