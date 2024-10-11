"""
This module handles the MongoDB connection using pymongo.
"""
from pymongo import MongoClient
from os import environ

# Global variable for MongoDB database

def connect_db():
    """
    Connect to MongoDB using MongoClient and set up a global `db` object.
    Replace 'your_mongo_uri' with your actual MongoDB connection string.
    """
    client = MongoClient(environ.get("MONGODB_URL", "mongodb+srv://sridhartalari53:NtmRxLpDfYTWwx9H@vodex.7tqts.mongodb.net/"))
    print("Connected to MongoDB")
    return client[environ.get("DATABASE_NAME", "vodex")]

DB = connect_db()