# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:15:38 2022

@author: anjana
"""

import pandas as pd
import json
import numpy as np
import py2neo

from neo4j import GraphDatabase
from pykeen.triples import TriplesFactory

host = 'bolt://localhost:7687'
user = 'neo4j'
password = '1234'
driver = GraphDatabase.driver(host,auth=(user, password))                                        

def run_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
       # print(pd.DataFrame([r.values() for r in result], columns=result.keys()))
        return pd.DataFrame([r.values() for r in result], columns=result.keys())

data = run_query("""MATCH (s)-[r]->(t) RETURN toString(id(s)) as source, toString(id(t)) AS target, type(r) as type""")
print(data.head())

##

print(data)

from pykeen.triples import TriplesFactory


tf = TriplesFactory.from_labeled_triples(
  data[["source", "type", "target"]].values,
  create_inverse_triples=False,
  entity_to_id=None,
  relation_to_id=None,
  compact_id=False,
  filter_out_candidate_inverse_relations=True,
  metadata=None,
)

print(tf)

#spliting dataset into train test validation set
training, testing, validation = tf.split([.8, .1, .1])

print(training, testing, validation)

##embeddings

from pykeen.pipeline import pipeline

result = pipeline(
    training=training,
    testing=testing,
    validation=validation,
    model='TransR',
    stopper='early',
    epochs=20,
    dimensions=512,
    random_seed=420

)

print(result)

##Multiclass link prediction
from pykeen.models.predict import get_tail_prediction_df

compound_id = run_query("""
Match (u:user) where u.name="A3I9GK5OO42B0I" return toString(id(u)) as id
""")['id'][0]


##predictions for also_view

df = get_tail_prediction_df(result.model, compound_id, 'also_view', triples_factory=result.training)
print(df.head(5))

##Store predictions to Neo4j

candidate_nodes = df[df['in_training'] == False].head(5)['tail_label'].to_list()

run_query("""
MATCH (n)
WHERE id(n) = toInteger($compound_id)
UNWIND $candidates as ca
MATCH (c)
WHERE id(c) = toInteger(ca)
MERGE (n)-[:PREDICTED_PRODUCT]->(c)
""", {'compound_id':compound_id, 'candidates': candidate_nodes})

##predictions for also_buy

df = get_tail_prediction_df(result.model, compound_id, 'also_buy', triples_factory=result.training)
print(df.head(5))

##Store predictions to Neo4j

candidate_nodes = df[df['in_training'] == False].head(5)['tail_label'].to_list()

run_query("""
MATCH (n)
WHERE id(n) = toInteger($compound_id)
UNWIND $candidates as ca
MATCH (c)
WHERE id(c) = toInteger(ca)
MERGE (n)-[:PREDICTED_PRODUCT]->(c)
""", {'compound_id':compound_id, 'candidates': candidate_nodes})

##predictions for belongsto

df = get_tail_prediction_df(result.model, compound_id, 'belongsto', triples_factory=result.training)
print(df.head(5))

##Store predictions to Neo4j

candidate_nodes = df[df['in_training'] == False].head(5)['tail_label'].to_list()

run_query("""
MATCH (n)
WHERE id(n) = toInteger($compound_id)
UNWIND $candidates as ca
MATCH (c)
WHERE id(c) = toInteger(ca)
MERGE (n)-[:PREDICTED_PRODUCT]->(c)
""", {'compound_id':compound_id, 'candidates': candidate_nodes})

##predictions for reviews

df = get_tail_prediction_df(result.model, compound_id, 'reviews', triples_factory=result.training)
print(df.head(5))

##Store predictions to Neo4j

candidate_nodes = df[df['in_training'] == False].head(5)['tail_label'].to_list()

run_query("""
MATCH (n)
WHERE id(n) = toInteger($compound_id)
UNWIND $candidates as ca
MATCH (c)
WHERE id(c) = toInteger(ca)
MERGE (n)-[:PREDICTED_PRODUCT]->(c)
""", {'compound_id':compound_id, 'candidates': candidate_nodes})

