# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:32:22 2022

@author: Karthik
"""

import pandas as pd
import numpy as np


df = pd.read_csv("kg_full.txt",sep=" ",header=None)
#with open('kg_full.txt') as fp:
    #df = fp.read()
print(df[0])
train, validate, test = np.split(df.sample(frac=1, random_state=42), [int(.6*len(df)), int(.8*len(df))])
print(train)
print(validate)
print(test)
print(df)
np.savetxt('kg1-train.txt', train.values, fmt="%d",delimiter = '\t')
np.savetxt(r'kg1-test.txt', validate.values, fmt='%d', delimiter = '\t')
np.savetxt(r'kg1-valid.txt', test.values, fmt='%d', delimiter = '\t')

