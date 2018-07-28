# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:50:29 2018

@author: daant
"""


import pickle 
import praw

objects = []
with (open("fullset.red", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
        
test = objects[0][0]


for obj in objects[0]:
    try:
        print(obj.url)
    except:
        print('no url')