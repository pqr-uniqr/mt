"""
Author: Hyun Sik Kim
Login: hk110
"machine translation" project for cs146 spring 2014

"""


#ISSUES:
#


import math
import sys

#given a parallel corpus (A,B) where A is in language a and B in b
#get tau_{a,b} for all pairs,
def param_est(f,e): #will give tau_(f,e)
#TODO Intial count
    #assuming initial tau of 1 for all pairs
    #for (a,b) for all a in sentence A and b in sentence B
    #dic[(a,b)]+=1
    #TODO design choice: {"le":{"the":30, "a": 10}} or {('le','the'):30, ('le','a'):10}

#TODO do EM 10 times
    #the E step

    pass


if __name__ = '__main__':
    #estimate parameters
    #if script demands so, use dumb decoding
