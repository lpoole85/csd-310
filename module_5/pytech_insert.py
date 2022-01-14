""" 
    Title: pytech_insert.py
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

""" three student documents"""
# Bob Jones's data document 
bob = {
    "student_id": "1007",
    "first_name": "Bob",
    "last_name": "Jones",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Kim Smith data document 
kim = {
    "student_id": "1008",
    "first_name": "Kim",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# Mark Paul data document
mark = {
    "student_id": "1009",
    "first_name": "Mark",
    "last_name": "Paul",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
bob_student_id = students.insert_one(bob).inserted_id
print("  Inserted student record Bob Jones into the students collection with document_id " + str(bob_student_id))

kim_student_id = students.insert_one(kim).inserted_id
print("  Inserted student record Kim Smith into the students collection with document_id " + str(kim_student_id))

mark_student_id = students.insert_one(mark).inserted_id
print("  Inserted student record Mark Paul into the students collection with document_id " + str(mark_student_id))

input("\n\n  End of program, press any key to exit... ")