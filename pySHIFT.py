"""
PySHIFT :: Scratch project for Python Timetable and Schedule Manager

CHANGELOG:
18052019
* Created the file

"""
import os
from itertools import permutations
import mysql.connector as cnx

# use mysql database for loading connection

currDir = os.getcwd()
print(currDir)
try:

    mydb = cnx.connect(
        user="newuser",
        passwd="password",
        database="my_db"
    )
    print("YUM")
    cur = mydb.cursor()
except:  # TODO HANDLE EXCEPT
    mydb = cnx.connect(
        user="newuser",
        passwd="password"

    )
    print("YAY")
    cur = mydb.cursor()
# init cnx as connection, cur as cursor
cur.execute("USE my_db")

# DECLARATION
subjects = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: ["English", "Physics", "Chemistry", "Biology", "Maths"],
    10: ["English", "Physics", "Chemistry", "Biology", "Maths"],
    11: {'SCI': ["English", "M/C", "B/C", "Physics", "Chemistry"],
         'COM': ["Subj1", "Subj2", "Subj3", "Subj4", "Subj5"],
         'HUM': ["Subj1", "Subj2", "Subj3", "Subj4", "Subj5"]},
    12: {'SCI': ["English", "M/C", "B/C", "Physics", "Chemistry"],
         'COM': ["Subj1", "Subj2", "Subj3", "Subj4", "Subj5"],
         'HUM': ["Subj1", "Subj2", "Subj3", "Subj4", "Subj5"]}
}
teachers = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None,
    11: None,
    12: None
}
