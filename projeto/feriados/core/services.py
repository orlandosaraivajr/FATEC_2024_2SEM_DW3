'''
https://pymongo.readthedocs.io/en/stable/tutorial.html
https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
'''
import pymongo
from pymongo import MongoClient

def inserir_mongo(dados):
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection
    posts = db.posts
    post_id = posts.insert_one(dados).inserted_id
    return post_id
