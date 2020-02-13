"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

tel_number_ist = []


def countDiffTelNumber(records):
    count = 0
    for item in records:
        if item[0] not in tel_number_ist:
            tel_number_ist.append(item[0])
            count += 1
        if item[1] not in tel_number_ist:
            tel_number_ist.append(item[1])
            count += 1
    return count

print("There are {} different telephone numbers in the records.".format(
    countDiffTelNumber(texts) + countDiffTelNumber(calls)))
