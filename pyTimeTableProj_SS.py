"""
@author : srevinsaju
@located in github/srevinsaju

Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux bash <ubuntu 18.04 LTS>
<JetBrains PyCharm 2019.1.2 (Community Edition)
Build #PC-191.7141.48, built on May 7, 2019
JRE: 11.0.2+9-b159.56 amd64
JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
Linux 4.18.0-18-generic>



PYTHON TIME TABLE CREATION ALGORITHM
# !!!! THIS PROGRAM IS IN ALPHA STAGE !!!
cheatSheet::
1 2 3 = 3
4 5 = 5
6 7 8 = 8
9 10 = 10
11 12 = 12

openfile var is used as file. File is in the form of Plain Text (UTF-8) Encoding::
<syntax> w = open(args)
Name of File is saved_db.brain
*.brain is official file extension for reread databases and RAW files.

the algorithm so far
# TODO please do this at the last :: handle exceptions :: handle except ListError
list --> permutation --> check priority --> (if xi and xii) --> block period
_____________________________________________________________________________________
*********************************************
CHANGELOG
*********************************************
08052019
* Added file to Github

10052019
* Bug fixes.

11052019
* Bug fixes
* Added MANUAL TimeTable editor through CLI

12052019
* Added file i/o operations in the *.brain file in the directory to prevent data loss
* Added exit option by 0 class enter on input option in __init__() function
* Added FileSystem Engine to read existing *.brain file changes and append to existing RAM (2158)

# * TODO add result dict conflict checker
*********************************************
-------------------------------------------------------------------------------------
"""

# import
from itertools import permutations

# appending or creating the file saved_db.brain
# a necessary brain declaration to prevent Exceptions of FileErrors.
# If not exist, python3 will automatically create one
brain = open('saved_db.brain', "a+")
brain.close()
# for safety
finished = []
paramNum = 0
subjects = {"xii_and_xi": ["M/C", "English", "Physics", "Chemistry", "B/C"]}
result = {}  # dictionary for handling different values
list_of_subjects = """
E:English
M:Maths / Computer @computer is deprecated only for class xii and xi code
P:Physics
C:Chemistry
B:Biology / Computer @computer is deprecated only for class xii and xi code
"""

# always launch FileSystem Engine on initiation
# Build! >>>
brain = open('saved_db.brain', "r+")
if (brain.readlines(1) == []):
    result = {}
else:
    s = str(brain.readlines(1))
    result = eval(s[2:-4])


def manipulate_manual(paramNum, paramtype):
    # this function is for manually manipulating the table::
    # the result is user defined
    # appending the result takes place in the last

    print("Time table configurator :: v1.0 Build 01")
    print("The notation for each subject is >> \n", list_of_subjects)
    print("The syntax is : \n E,M,B,C,P,P,C\nsyntax for writing config. "
          "No whitespace permitted. 7 periods are supposed to be there")
    user_io = input("class" + str(paramNum) + ">>> ")
    user_io = user_io.strip()
    if (len(user_io) != 13):
        print("Invalid User input! Quitting")
        return None
    else:
        user_io = user_io.replace("E", "English")
        user_io = user_io.replace("C", "Chemistry")
        user_io = user_io.replace("M", "M/C")
        user_io = user_io.replace("B", "B/C")

        user_io = user_io.replace("P", "Physics")
        # TODO other subjects as we progress
        user_eval = user_io.split(",")
        print(user_eval)
        if (input("Is this representation favored?") == "y"):
            # check conflict exist

            brain = open('saved_db.brain', "a+")
            print("Ok! Adding current list to prebuilt timetable list for analysis")
            result[str(paramNum) + paramtype] = user_eval
            print(result)
            finished.append(str(paramNum) + paramtype)
            # no chaos, just a simple syn
            brain.write("{'" + str(paramNum) + paramtype + "': "
                        + str(result[str(paramNum) + paramtype]) + "}\n")
            # convert to unicode dictionary
            brain.close()
        else:
            # TODO please check else statement, Call function within another function
            print('Retrying...')
            manipulate_manual(paramNum, paramtype)
        print("Exiting manual timetable builder CLI")

        __init__()


def blckPeriod(result, paramNum, paramtype):
    tempBlock = None
    count = 0
    if (len(result[str(paramNum) + paramtype]) < 7):
        print("blckPeriod Algorithm loaded")
        for i in result[str(paramNum) + paramtype]:
            if (i == "English"):
                count += 1
            else:
                boolYorN = input("Is " + i + " sir / teacher free for the next period, " +
                                 "so that a block period can be assigned ? (y/n) >>> ")
                if (boolYorN == "y"):
                    result[str(paramNum) + paramtype] = result[str(paramNum) + paramtype][:count] + \
                                                        result[str(paramNum) + paramtype][count:count + 1] + \
                                                        result[str(paramNum) + paramtype][count:]
                    print(result[str(paramNum) + paramtype])
                    count += 1
                    print(count)
                else:
                    count += 1

    else:
        result[str(paramNum) + paramtype] = tempBlock


# PARSE PART
# parse user input to code::
# +++++++++++++++++++++++++++++++


def parse_io(priority):
    if (priority == "E"):
        priority = "English"
        return priority
    elif (priority == "M"):
        priority = "M/C"
        return priority
    elif (priority == "P"):
        priority = "Physics"
        return priority
    elif (priority == "C"):
        priority = "Chemistry"
        return priority
    elif (priority == "B"):
        priority = "B/C"
        return priority
    else:
        priority = 0
        print("Sorry! Invalid Input. Probably this is an error on our side")
        return priority


def priority_io():
    priority = input("Choose the subject or the subject teacher who has priority 1 (high)" + \
                     list_of_subjects + ">>> ")
    teacherName = input("Enter the name of the teacher >>>")
    p0priority = int(input("Enter the position of the period (1-7)"))
    return priority, p0priority, teacherName


def manipulate_timetable(param, param0, paramtype=""):  # usage : manipulate_timetable(param<class>)
    print("Loading Algorithm...")
    tempResult = []
    # TODO do algorithm
    # create permutation of the list of subjects
    # syntax for accessing items in the dictionary < syntax : subjects[xii_and_xi]
    print("*" * 30)
    print("Compiling time table for ", param0, paramtype)
    subjects_in_class = subjects[param]
    subject_permutation = list(permutations(subjects_in_class))
    if (result == {}):

        # check priority and ask for the subjection and period position
        priority, p0priority, teacherName0 = priority_io()

        priority = parse_io(priority)
        priority1, p1priority, teacherName1 = priority_io()
        priority1 = parse_io(priority1)
        pass
    else:
        # TODO later
        print("#TODO")
        return 0

    for set_of_period in subject_permutation:
        if (set_of_period[p0priority - 1] == priority):
            if (set_of_period[p1priority - 1] == priority1):
                print(set_of_period)
                tempResult.append(set_of_period)
            else:
                print(end="")
        else:
            print(end="")
    count = 0
    for tempSetOfPeriod in tempResult:
        count += 1
        print("[", count, "] >>> ", tempSetOfPeriod)
    num = int(input("Please view and choose the most appropriate" +
                    "schedule for adding block periods / optionals >>> "))
    result[str(paramNum) + paramtype] = tempResult[num]
    print('The list for ', paramNum, paramtype, " is :", result)

    # PROCEED TO BLOCK PERIOD OR OPTIONALS == TODO
    if (paramNum == 11 or paramNum == 12):
        print("Loading algorithm for block period...")
        blckPeriod(result, paramNum, paramtype)
    else:
        # TODO not yet
        print("INFO [1] # TODO ")


def __init__():
    print("""PYTHON TIME TABLE CREATION ALGORITHM""")
    print("Enter 0 if you wish to quit")
    runClass = int(input("Enter the class for time table manipulation first:>>> "))
    if (runClass == 0):
        return False
    if (runClass == 11 or runClass == 12):
        paramtype = input("Enter the group :: <S:Science Group, C:Commerce, H:Humanities")
        if (paramtype == "S"):
            paramtype = "Science"
        elif (paramtype == "C"):
            paramtype = "Commerce"
        elif (paramtype == "H"):
            paramtype = "Humanities"
        else:
            print("Error! invalid input!")

        param = "xii_and_xi"
        paramNum = 12

    else:
        param = "sth"
        # TODO
        paramNum = 0
        paramtype = ""

    if (runClass == 12):
        resp = input("Do you want to create the time table for class :" + str(runClass)
                     + " manually? >>>")
        if (resp == "y"):
            manipulate_manual(paramNum, paramtype)
        else:
            manipulate_timetable(param, paramNum, paramtype)


__init__()
