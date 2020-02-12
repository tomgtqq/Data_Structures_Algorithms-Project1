"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


def findLongestCallDuration(records):
    total_time = 0
    tel_number = ""
    for item in records:
        if int(item[3]) > total_time:
            total_time = int(item[3])
            tel_number = item[0]
    return tel_number, total_time


def testFindLongestCallDuration():

    records = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
               ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
               ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975']]

    assert(findLongestCallDuration(records) == ('78298 91466', 2093))
    print("function is working correctly!")


testFindLongestCallDuration()


print("%s spent the longest time, %s seconds, on the phone during September 2016." %
      findLongestCallDuration(calls))
