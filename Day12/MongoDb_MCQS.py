import csv

# Define the MCQs
mcqs = [
    {"question": "What is MongoDB?", "options": ["A database", "A programming language", "A web framework", "A text editor"], "correct": "A database", "difficulty": "easy"},
    {"question": "Which data format does MongoDB use?", "options": ["JSON", "XML", "CSV", "YAML"], "correct": "JSON", "difficulty": "easy"},
    {"question": "What is a document in MongoDB?", "options": ["A row in a table", "A column in a table", "A JSON-like object", "A database schema"], "correct": "A JSON-like object", "difficulty": "easy"},
    {"question": "Which method is used to insert a document in MongoDB?", "options": ["insert()", "add()", "insertOne()", "push()"], "correct": "insertOne()", "difficulty": "easy"},
    {"question": "Which command is used to view all databases in MongoDB?", "options": ["show databases", "list databases", "db.getDatabases()", "db.show()"], "correct": "show databases", "difficulty": "easy"},
    {"question": "What is a collection in MongoDB?", "options": ["A database", "A table", "A field", "A function"], "correct": "A table", "difficulty": "easy"},
    {"question": "How do you update a document in MongoDB?", "options": ["update()", "updateOne()", "modify()", "set()"], "correct": "updateOne()", "difficulty": "medium"},
    {"question": "Which of the following is true about MongoDB's schema design?", "options": ["Schema is rigid", "Schema is flexible", "Schema is non-existent", "Schema is predefined"], "correct": "Schema is flexible", "difficulty": "medium"},
    {"question": "What is the default port for MongoDB?", "options": ["27017", "3306", "5432", "8080"], "correct": "27017", "difficulty": "medium"},
    {"question": "Which of the following is a valid data type in MongoDB?", "options": ["String", "Date", "ObjectId", "All of the above"], "correct": "All of the above", "difficulty": "medium"},
    {"question": "Which command is used to remove a document in MongoDB?", "options": ["delete()", "remove()", "deleteOne()", "erase()"], "correct": "deleteOne()", "difficulty": "medium"},
    {"question": "How do you retrieve documents in MongoDB?", "options": ["get()", "find()", "retrieve()", "fetch()"], "correct": "find()", "difficulty": "medium"},
    {"question": "What is sharding in MongoDB?", "options": ["Data replication", "Data partitioning", "Data backup", "Data indexing"], "correct": "Data partitioning", "difficulty": "medium"},
    {"question": "Which function is used to join collections in MongoDB?", "options": ["join()", "merge()", "aggregate()", "link()"], "correct": "aggregate()", "difficulty": "medium"},
    {"question": "What is the purpose of an index in MongoDB?", "options": ["To backup data", "To replicate data", "To improve query performance", "To enforce schema"], "correct": "To improve query performance", "difficulty": "medium"},
    {"question": "What is a replica set in MongoDB?", "options": ["A set of related documents", "A set of related collections", "A group of MongoDB servers", "A set of indexes"], "correct": "A group of MongoDB servers", "difficulty": "hard"},
    {"question": "Which command is used to start the MongoDB server?", "options": ["mongod", "mongo", "mongodb", "startmongo"], "correct": "mongod", "difficulty": "hard"},
    {"question": "How do you create a text index in MongoDB?", "options": ["db.collection.createIndex({field: 'text'})", "db.collection.createTextIndex({field: 1})", "db.collection.createIndex({field: 'text'})", "db.collection.addIndex({field: 'text'})"], "correct": "db.collection.createIndex({field: 'text'})", "difficulty": "hard"},
    {"question": "Which command is used to back up a MongoDB database?", "options": ["mongobackup", "mongodump", "mongorestore", "mongosave"], "correct": "mongodump", "difficulty": "hard"},
    {"question": "What is the role of the config servers in a MongoDB sharded cluster?", "options": ["Store data", "Store metadata and configuration settings", "Backup data", "Handle queries"], "correct": "Store metadata and configuration settings", "difficulty": "hard"},
    {"question": "Which method is used to perform a bulk insert in MongoDB?", "options": ["insertMany()", "bulkInsert()", "insertMultiple()", "insertAll()"], "correct": "insertMany()", "difficulty": "hard"},
    {"question": "How do you list all collections in a MongoDB database?", "options": ["show collections", "list collections", "db.getCollections()", "db.showCollections()"], "correct": "show collections", "difficulty": "hard"},
    {"question": "What is the storage engine used by default in MongoDB?", "options": ["WiredTiger", "InnoDB", "MyISAM", "LevelDB"], "correct": "WiredTiger", "difficulty": "hard"},
    {"question": "Which MongoDB utility is used for monitoring and managing MongoDB deployments?", "options": ["mongodump", "mongoimport", "mongostat", "mongotop"], "correct": "mongostat", "difficulty": "hard"},
    {"question": "What is a capped collection in MongoDB?", "options": ["A fixed-size collection", "A read-only collection", "A collection without indexes", "A collection with unlimited size"], "correct": "A fixed-size collection", "difficulty": "hard"},
    {"question": "How do you enable authentication in MongoDB?", "options": ["Use --auth option", "Use --secure option", "Use --enableAuth option", "Use --login option"], "correct": "Use --auth option", "difficulty": "hard"},
    {"question": "Which command is used to restore a MongoDB database?", "options": ["mongorestore", "mongobackup", "mongoload", "mongorecover"], "correct": "mongorestore", "difficulty": "hard"},
    {"question": "What is the oplog in MongoDB?", "options": ["Operational log for tracking changes", "Error log for MongoDB", "Performance log for queries", "Transaction log"], "correct": "Operational log for tracking changes", "difficulty": "hard"},
    {"question": "Which MongoDB operator is used for pattern matching?", "options": ["$match", "$search", "$regex", "$find"], "correct": "$regex", "difficulty": "hard"},
    {"question": "What is the purpose of the `$lookup` operator in MongoDB?", "options": ["To join collections", "To filter documents", "To sort documents", "To group documents"], "correct": "To join collections", "difficulty": "hard"},
    {"question": "Which method is used to convert a JSON string to a BSON object in MongoDB?", "options": ["JSON.parse()", "BSON.convert()", "ObjectId()", "toBSON()"], "correct": "ObjectId()", "difficulty": "hard"},
]

# Create the CSV file
csv_file = "mongodb_mcqs.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Question", "Option1", "Option2", "Option3", "Option4", "Correct Answer", "Difficulty"])
    # Write the MCQs
    for mcq in mcqs:
        writer.writerow([mcq["question"], mcq["options"][0], mcq["options"][1], mcq["options"][2], mcq["options"][3], mcq["correct"], mcq["difficulty"]])

print(f"CSV file '{csv_file}' generated successfully!")
