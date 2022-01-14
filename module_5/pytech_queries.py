""" 
    Title: pytech_queries.py
    Name: Lindsay Poole
    Module: 5.3
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.dtenb.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
kim = students.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + kim["student_id"] + "\n  First Name: " + kim["first_name"] + "\n  Last Name: " + kim["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")