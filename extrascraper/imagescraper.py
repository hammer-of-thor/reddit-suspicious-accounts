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
            objects = pickle.load(openfile)
        except EOFError:
            break

img_exts = ['jpeg','jpg','png','gmp','tiff']
        
for obj in objects:
    url = []
    try:
        #print(obj.url)
        url = obj.url
    except:
        url = []
    if str(url[-3:]) in img_exts or str(url[-4:]) in img_exts:
        print(url)