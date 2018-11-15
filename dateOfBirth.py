# Coding prompt:
#
# Our team typically celebrates teammates' birthdays at the end of the month.  We have a roster
# of teammates and their birthdays in a comma-separated text file, with contents like below:
#
# Andrew, 06-03-1990
# Victor, 12-03-1989
# Sandra, 07-31-1991
# John,   06-12-1992

#
# Your task is to create a function that takes 2 parameters: path to the roster file, and a month of the
# year
# Your function should return the list of teammates born in the given month
#
# Sample python function declaration below
import os


def findTeammatesBornInMonth(roster, month):
    '''Implementation here'''
    if not isinstance(month, int):
        return -1
    else:
        dob = {}
        try:
            # abspath = os.path.abspath(roster)
            if os.path.isfile(roster):
                with open(roster, "r") as fp:
                    data = fp.readlines()
                    for line in data:
                        if line not in ['\n', '\r\n']:
                            name, birthdate = line.split(',')  # ['Andrew', ' 06-03
                            str_mon = birthdate.strip().split('-')[0]
                            int_mon = int(str_mon)
                            if int_mon in dob:
                                dob[int_mon].append(name)  # {6:['Andrew','John']}
                            else:
                                dob[int_mon] = [name]  # {6:['Andrew']}
        except IOError as e:
            print("I/O Error: (%s)" % e)
        if month >= 1 and month <= 12:
            return dob[month]
        else:
            return "Invalid Month: {0}".format(month)


print(findTeammatesBornInMonth('test.csv', 6))
# file ends with csv
# validate month value [1-12]
# date format (MM-DD-YYYY)
# file data
