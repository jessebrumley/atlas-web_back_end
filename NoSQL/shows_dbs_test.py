#!/usr/bin/env python3
from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# List all databases
databases = client.list_database_names()

# Print each database
for db in databases:
    print(db)
