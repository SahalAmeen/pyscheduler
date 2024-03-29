"""
PySHIFT :: Scratch project for Python Timetable and Schedule Manager

SYNTAX on MYSQL::
teachers (name_ VARCHAR (20), sub VARCHAR (10), class_ INT)

CHANGELOG:
18052019
* Created the file

"""
import os
from itertools import permutations
import mysql.connector as cnx
from random import randint

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
"""
# <editor-fold desc="Description">
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
# </editor-fold>"""  # in case of emergency


def engine(class_, opt=None):
    print('Engine Loaded!')
    # generate a weeks timetable randomly.
    # 7*6 = 42, 5*6=30 + 5 = 35 + 5 = # # # 40 + 1games + 1Rnd subject
    # TODO CHECK conflict
    tempList = []
    count = randint(0, 4)
    count2 = randint(1, 5)
    if (opt == None):
        subjectTemp = subjects[class_]
        pass
    else:
        subjectTemp = subjects[class_][opt]
        pass
    if (len(subjectTemp) == 5):
        for i in range(len(subjectTemp)):
            if (count == 5):
                count = 0
            if (count2 == 6):
                count2 = 1

            Tem = subjectTemp + subjectTemp[count:count + 1] + subjectTemp[count2 - 1:count2]
            print(Tem)
            tempList.append(Tem)
            count += 1
            count2 += 1
        """
        part0 = tempList[randint(0, len(tempList) - 1)]
        temp0 = list(permutations(part0))
        """
        final = []
        for i in range(0, 5):
            j = list(permutations(tempList[i]))

            final.append(j[randint(0, len(j) - 1)])

        print(final, sep="\n")
        pass


def decompiler():
    print()


def __init__():
    print("PYSHIFT Build 1.0")
    # check number of teachers:
    class_ = 12
    opt = "SCI"
    engine(class_, opt)
    print()


__init__()
