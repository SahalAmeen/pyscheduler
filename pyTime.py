from itertools import permutations as perm

# result = predefine
result = [""]


def xii(result):
    running = True
    subjects = ["English", "M/C", "B/C", "Physics", "Chemistry"]
    count = 0
    loopCount = 0
    priorityrun = True
    runtime = 0
    # init

    aday = list(perm(subjects))

    def createPermSub(period, count=0, runtime=0, running=True, loopCount=0):
        tmpresult = []
        while (running):
            # get teacher priority

            if ((len(period)) < 7):
                if (period[count] == "English"):
                    # reject "English" (as it doesn't need block periods)
                    count += 1
                ask_first = input(
                    "Is " + period[count] + " sir / teacher free for the next \
                    period? (y/n)")
                if (ask_first == "y"):
                    # append indes period to the consecutive period
                    print("Adding ", period[count],
                          " for the consecutive period")
                    # manipulate permuted tuple
                    period = period[0:count] + \
                             period[count:count + 1] + period[count:]
                    print(period)
                    count += 2
                elif (ask_first == "n"):
                    count += 1
                else:
                    # check if input is not matching criteria (handle except)
                    # TODO handle except
                    print('Invalid Input. Quitting')
                    break
            else:
                runtime += 1
                result.append(period)
                print("FINAL LIST {", loopCount + 1, "} ", result[runtime])
                loopCount += 1

                return running
            return running
        return running

    def createPerm(running=True, loopCount=0):
        # check priority check over here
        tmpresult = []  # init tmpresult variable to hold useless stuff
        priority = input("Enter the subject for which the corresponding \
                                    teacher has priority \
                                    \n E:English \n M:Math-Csc \n B:Bio-Csc \n \
                                    P:Physics \
                                    \n C:Chemistry")
        priorityorder = int(
            input("Enter the position of the priority period (1-7)"))
        # assign priorit orig name from user input
        # Actually, this is  small code:
        if (priority == "E"):
            priority = "English"
        elif (priority == "M"):
            priority = "M/C"
        elif (priority == "B"):
            priority = "B/C"
        elif (priority == "P"):
            priority = "Physics"
        elif (priority == "C"):
            priority = "Chemistry"
        else:
            print("Invalid Syntax! Code : 0x0000001")

        for period in aday:
            if (priorityrun):
                if (period[priorityorder - 1] == priority):
                    print("INFO [1] ENTER PRIORITY BLOCK")
                    tmpresult.append(period)
                    print("Appended tmpresult : ", tmpresult)
                elif (period[priorityorder - 1] != priority):
                    print("INFO [2] NOT EQUAL. REMOVE PERMUTATION FROM LIST")
                else:
                    print("Not entered priority block")

        for period in aday:
            print(period)
        for period in aday:
            print("initial permutation of a schedule :", period)
            createPermSub(period, count, runtime, running, loopCount)
        print("SSSSSSS", result)

    createPerm(running, loopCount)


def __main__(result):
    print(""" TIME TABLE ALGORITHM """)
    class_ = int(
        input("Enter the class for which the ime table is to be calculated >>>"))
    if (class_ == 12 or class_ == 11):
        print("Class XIth - Science and Class XII th - Science have to be compiled together. Proceed?")
        if (input("(y/n)") == "y"):
            # TODO implementation for class XIIth due to priority
            # TODO implementation fot class XIth due to lower priority
            print("Begin compile ...")
            # 12th
            tmpresult = xii(result)
            result = tmpresult
            # proceed to XI th

        else:
            print("stop")


__main__(result)
