# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:59:59 2018

@author: daant
"""

import pandas as pd

seed = pd.read_csv(r'F:\CloudStation\Educational\Git\reddit-suspicious-accounts\seed.csv', header=None)

import praw

reddit = praw.Reddit(client_id='XXXX-Fg', client_secret='XXXX',
                      user_agent='PC:XXX:0.1 (by /u/XX-X)')

go_crawl = False
    
import pickle 

if go_crawl:   
    subs = []    
    
    for r, user in seed.iterrows():
        try:
            for submission in reddit.redditor(user[0]).new(limit=None):
                #print(submission.title)
                subs.append(submission)
        except:
            print(user[0])
    
    with open('fullset.red', 'wb') as pickle_file:
        pickle.dump(subs, pickle_file)       
else:
    objects = []
    with (open("fullset.red", "rb")) as openfile:
        while True:
            try:
                objects = pickle.load(openfile)
            except EOFError:
                break
            
crawl_parents = True