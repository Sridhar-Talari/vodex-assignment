from pymongo import MongoClient

# Replace with your connection string
# mongo_uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority"
mongo_uri = "mongodb+srv://sridhartalari53:NtmRxLpDfYTWwx9H@vodex.7tqts.mongodb.net/"

client = MongoClient(mongo_uri)

# Access the database
db = client['vodex']

# Example: Access a collection, will be created automatically if it doesn't exist
collection = db['items']

# Insert a new document (collection will be created if it doesn't exist)
new_document = {
  "name": "string",
  "email": "string",
  "item_name": "string",
  "quantity": 1,
  "expiry_date": "2024-10-11"
}
insert_result = collection.insert_one(new_document)

# Print the inserted document's ID
print(f"Inserted document ID: {insert_result.inserted_id}")

# Perform find operation to verify the insertion
document = collection.find_one({"name": "string"})
print(document)
