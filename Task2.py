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
tel_numbers = set()
tel_number_total_time = dict()


def createTelNumbersSet(records):
    for item in records:
        tel_numbers.add(item[0])
        tel_numbers.add(item[1])


def createTelNumTotalTimeDict(num_list, records):
    for num in num_list:
        total_time = calculateSpentTime(num, records)
        tel_number_total_time[num] = total_time


def calculateSpentTime(num, records):
    spent_time = 0
    for item in records:
        if item[0] == num:
            spent_time += int(item[3])
        if item[1] == num:
            spent_time += int(item[3])

    return spent_time


createTelNumbersSet(calls)

createTelNumTotalTimeDict(tel_numbers, calls)

telephone_number = sorted(tel_number_total_time, key=(
    lambda key: tel_number_total_time[key]), reverse=True)[0]

total_time = tel_number_total_time[str(telephone_number)]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    telephone_number, total_time))
