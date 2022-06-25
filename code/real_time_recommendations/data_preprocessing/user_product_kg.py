# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:32:36 2022

@author: anjana
"""

import pandas as pd
import json
import numpy as np

import py2neo


df = pd.read_json('video.json', lines=True)
print(df)
graph = py2neo.Graph(password = "1234")
#users = dict(graph.evaluate('MATCH (n:user) RETURN n'))
#products = dict(graph.evaluate('MATCH (n:product) RETURN n'))

users = dict()
products = dict()

length = len(df.index)
for i in range(length):
#for i in range(df.shape[0]):
  ID = df["reviewerID"][i]
  if(ID in users):
    uNode = users[ID]
  else:
    uNode = py2neo.Node("user",name = str(df["reviewerID"][i]))
    users[ID] = uNode

  ID = df["asin"][i]
  if(ID in products):
    pNode = products[ID]
  else:
    pNode = py2neo.Node("product",name = str(df["asin"][i]))
    products[ID] = pNode
  
  rShip = py2neo.Relationship(uNode,"reviews",pNode)
  print(rShip)
  graph.create(rShip)
  
for i in range(length):
#for i in range(df.shape[0]):
  ID = df["reviewerID"][i]
  if(ID in users):
    uNode = users[ID]
  else:
    uNode = py2neo.Node("user",name = str(df["reviewerID"][i]))
    users[ID] = uNode

  ID = df["asin"][i]
  if(ID in products):
    pNode = products[ID]
  else:
    pNode = py2neo.Node("product",name = str(df["asin"][i]))
    products[ID] = pNode
  
  rShip = py2neo.Relationship(uNode,"reviews",pNode)
  print(rShip)
  graph.create(rShip)