from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

# Load environment variables from the .env file
load_dotenv()

# Get MongoDB connection string from environment variables
connection_string = os.getenv('MONGODB_CONNECTION_STRING')

# Connect to the MongoDB server using the connection string and access the database named as 'database' 
client = MongoClient(connection_string)
db = client['database']  

def insert_data(collection_name, json_file_path, unique_fields):
    """
    This function reads data from a JSON file and attempts to insert it into the specified MongoDB collection. 
    If the collection is empty, all documents from the file are inserted. 
    If the collection already contains data, the function checks for duplicates using the provided unique fields 
    and only inserts non-duplicate documents.

    Args:
        collection_name (str): 
            The name of the MongoDB collection where the data will be inserted.
        json_file_path (str): 
            The file path to the JSON file containing the data to be inserted. The file should contain an array of JSON objects.
        unique_fields (list of str): 
            A list of field names that uniquely identify a document. Used to check for duplicates before insertion.
    
    Raises:
        FileNotFoundError: 
            If the specified JSON file is not found.
        json.JSONDecodeError: 
            If the JSON file contains invalid JSON.
        KeyError: 
            If any document in the JSON file does not contain one of the specified unique fields (when duplicates are being checked).
        pymongo.errors.PyMongoError: 
            If there is an error interacting with the MongoDB database.
    """
    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Insert data into the specified collection
    collection = db[collection_name]

    # Check if the collection is empty
    if collection.count_documents({}) == 0:
        # If empty, insert all documents
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} documents into {collection_name}.")
    else:
        # If not empty, check for duplicates based on unique fields
        inserted_count = 0
        for item in data:
            if all(field in item for field in unique_fields):
                query = {field: item[field] for field in unique_fields}
                existing_item = collection.find_one(query)
                if existing_item:
                    print(f"Item with {', '.join([f'{field} {item[field]}' for field in unique_fields])} already exists. Skipping.")
                else:
                    collection.insert_one(item)
                    inserted_count += 1
                    print(f"Inserted item with {', '.join([f'{field} {item[field]}' for field in unique_fields])}.")

        print(f"Inserted {inserted_count} new documents into {collection_name}.")

    # Check the total count of documents in the collection
    count = collection.count_documents({})
    print(f"Total documents in {collection_name} after insertion: {count}")

# Insert training completion certificates
insert_data('trainingCertificates', './Training Program Data/training_info.json', 'Email')

# Insert internship completion certificates
insert_data('internshipCertificates', './Internship Data/internship_info.json', 'Internship Id')

# Close the connection
client.close()