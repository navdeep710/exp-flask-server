import persistqueue
import random

mqueue = persistqueue.UniqueQ("random",multithreading=True)


def getrandomstring(length=10):
    mstring = "abcdefghijklmnopqrstuvqxyz123456789"
    return "".join([mstring[random.randint(0,34)] for x in range(length)])


def populatequeue(numentries=100):
    for i in range(numentries):
        mqueue.put(getrandomstring())

def getvalue():
    return mqueue.get()

def getvalues(numvalues):
    return [getvalue() for x in range(numvalues)]