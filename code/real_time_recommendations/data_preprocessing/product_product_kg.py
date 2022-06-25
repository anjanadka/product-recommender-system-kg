# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 23:13:44 2022

@author: anjana
"""

import pandas as pd
import json
import numpy as np

import py2neo

df = pd.read_json('data_video.json', lines=True)
graph = py2neo.Graph(password = "1234")

existing_product_nodes = graph.evaluate('MATCH (n:product) RETURN n')
product_list = list(dict(existing_product_nodes).values())
print(dict(existing_product_nodes))

#c = py2neo.Node("category",name = df['category'][1][1] )
#p = py2neo.Node("product", name = df['asin'][1]  )
#reln1 = py2neo.Relationship(p,"belongsto",c)
#graph.create(reln1)

existing_cat_nodes = graph.evaluate('MATCH (n:category) RETURN n')
cat_list = list(dict(existing_cat_nodes).values())


length = len(df.index)

for i in range(0,length) :
    product = df['asin'][i]
    cat = df['category'][i]
    if product in product_list :
        query = "MATCH (p:product {name: '"+product+"'}) RETURN p"
        product_node = graph.evaluate(query)
        #print(product_node)
    else :
         product_node = py2neo.Node("product",name = product )
         product_list.append(product)
    for j in cat : 
        if j == '</span></span></span>':
            break;
        else:
            if j in cat_list :
                query = "MATCH (p:category {name: '"+j+"'}) RETURN p"
                cat_node = graph.evaluate(query)
            else :
                 cat_node = py2neo.Node("category",name = j )
                 cat_list.append(j)
                 
            print(product_node,"belongsto",cat_node)
            reln1 = py2neo.Relationship(product_node,"belongsto",cat_node)
            walk1 = py2neo.walk(reln1)
            graph.create(reln1)
    ab = df['also_buy'][i]
    for j in ab:
        product1 = j
        if product1 in product_list :
            query = "MATCH (p:product {name: '"+product1+"'}) RETURN p"
            product1_node = graph.evaluate(query)
            print(product1_node)
        else :
            product1_node = py2neo.Node("product",name = product1 )
            print(product1_node)
            product_list.append(product1)
        reln2 = py2neo.Relationship(product_node,"also_buy",product1_node)
        walk2 = py2neo.walk(reln2)
        graph.create(reln2)
    
    av=df['also_view'][i]
    for j in av:
         product1 = j
         if product1 in product_list :
            query = "MATCH (p:product {name: '"+product1+"'}) RETURN p"
            product1_node = graph.evaluate(query)
            #print(product_node)
         else:
            product1_node = py2neo.Node("product",name = product1 )
            product_list.append(product1)
         reln3 = py2neo.Relationship(product_node,"also_view",product1_node)
         walk3 = py2neo.walk(reln3)
         graph.create(reln3)
    
    
    
    
        