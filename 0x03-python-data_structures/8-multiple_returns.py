#!/usr/bin/python3
def multiple_returns(sentence):
    myTuple = ()
    if len(sentence) == 0:
        myTuple = 0, "None"
    else:
        myTuple = len(sentence), sentence[0]
    return myTuple
