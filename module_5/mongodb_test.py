""" 
    Title: mongodb_test.py
    Name: Lindsay Poole
    Assignment: 5.2
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.dtenb.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections 
print(db.list_collection_names())
