# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:59:59 2018

@author: daant
"""

import pandas as pd

seed = pd.read_csv(r'F:\CloudStation\Educational\Git\reddit-suspicious-accounts\seed.csv', header=None)

import praw

reddit = praw.Reddit(client_id='xxx-Fg', client_secret='xxxx',
                      user_agent='PC:xxx:0.1 (by /u/xx-x)')

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
    subs = []
    with (open("fullset.red", "rb")) as openfile:
        while True:
            try:
                subs = pickle.load(openfile)
            except EOFError:
                break
            
crawl_parents = True
if crawl_parents:
    parents = []
    for sub in subs:
        if str(type(sub).__name__) == 'Comment':
            #print(sub)
            #print(sub.submission)
            test = praw.models.Submission(reddit, id=sub.submission)
            parents.append(test)
            
        with open('parents.red', 'wb') as pickle_file:
            pickle.dump(parents, pickle_file)       
else:
    parents = []
    with (open("parents.red", "rb")) as openfile:
        while True:
            try:
                parents = pickle.load(openfile)
            except EOFError:
                break
        