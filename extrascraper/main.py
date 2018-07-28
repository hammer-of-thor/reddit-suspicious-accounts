# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:59:59 2018

@author: daant
"""

import pandas as pd

seed = pd.read_csv(r'F:\CloudStation\Educational\Git\reddit-suspicious-accounts\seed.csv', header=None)

import praw

reddit = praw.Reddit(client_id='#######', client_secret='##########',
                      user_agent='PC:###:0.1 (by /u/###-####)')

subs = []    

for r, user in seed.iterrows():
    try:
        for submission in reddit.redditor(user[0]).new(limit=None):
            #print(submission.title)
            subs.append(submission)
    except:
        print(user[0])

import pickle 

pickle.dump(subs, 'fullset.red')

with open('fullset.red', 'wb') as pickle_file:
    pickle.dump(subs, pickle_file)