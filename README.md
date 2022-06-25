# Building a Product Recommender System Using Knowledge Graph Embedding and Graph Completion

Building an effective product recommender system using knowledge graph embedding method that reflects richer data inter-relationships and an efficient learning pipeline that can predict the user preferences with good precision.

## Objective

* Our project aim to construct and design a knowledge representation that encodes complex data inter-relationships using an unstructured raw dataset on user, product and category relationships.
* From the knowledge representation as defined above, we experiment to learn good representations that suit for passing to a machine learning pipeline.
* Using the learned representations, this project aims to predict the user preferences with good precision and evaluate the overall system performance.

## Dataset

* The dataset used in this project is [amazon review dataset](https://nijianmo.github.io/amazon/index.html).
* It comprises of data such as review data and product metadata.
* It contains a total of 233.1 million reviews and data collected is from May 1996 to October 2018.
* The dataset contains information on 29 different categories of products. The subset chosen for this work is “Video games”.

## Tools

* Python
* Neo4j
* Scipy
* Pykg2vec
* Py2neo
* PyKEEN

## System Architecture

![alt text](https://github.com/anjanadka/product-recommender-system-kg/blob/main/system_architecture/system_architecture.png)

## References

1. McAuley, Julian, Christopher Targett, Qinfeng Shi, and Anton Van Den Hengel. "Image-based recommendations on styles and substitutes." In Proceedings of the 38th international ACM SIGIR conference on research and development in information retrieval (2015) : 43-52.
2. Yu, Shih-Yuan, Sujit Rokka Chhetri, Arquimedes Canedo, Palash Goyal, and Mohammad Abdullah Al Faruque. "Pykg2vec: A Python Library for Knowledge Graph Embedding." J. Mach. Learn. Res. 22 (2021): 1-16.
3. Lucas Hu, Thomas Kipf, & Gökçen Eraslan. lucashu1/link-prediction: v0.1: FB and Twitter Networks. Zenodo.(2018): 1-14.
4. Mehdi Ali, Max Berrendorf, Charles Tapley Hoyt, Laurent Vermue, Sahand Sharifzadeh, Volker Tresp, and Jens Lehmann. Pykeen 1.0: A python library for training and evaluating knowledge graph embeddings. J. Mach. Learn. Res., 22(82):1–6, 2021.

