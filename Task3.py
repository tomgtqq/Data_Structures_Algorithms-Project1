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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A:

area_codes = []


def extractPrefixesCodes(record):
	if record[:3] == '140':
		return '140'
	elif record[:1] in ['7','8','9']:
		return record.split(' ')[0]
	elif record.index(')'):
		return record[:record.index(')')+1]
	


def testPartA():
    assert(extractPrefixesCodes('(080)43215621') == '(080)')
    assert(extractPrefixesCodes('(04344)211113') == '(04344)')
    assert(extractPrefixesCodes('78130 00821') == '78130')
    assert(extractPrefixesCodes('1408371942') == '140')

    print("Congratulations! Your extractPrefixesCodes")


testPartA()

for item in calls:
	if extractPrefixesCodes(item[0]) == '(080)':
		area_codes.append(extractPrefixesCodes(item[1]))

print("The numbers called by people in Bangalore have codes:",*sorted(set(area_codes)), sep = '\n')


#Part B:

calling_by_Bangalore = []

def extractCallsByBangalore(records):
	calls_list = []
	for item in records:
		if extractPrefixesCodes(item[0]) == '(080)':
				calls_list.append(item)
	return calls_list

def testPartB():
	records = [['(080)45291968','90365 06212','01-09-2016 06:30:36','9'],
			   ['(04344)228249','(080)43901222','01-09-2016 06:50:04,2329'],
			   ['1408371942','81529 57063','01-09-2016 10:17:21','46'],
			   ['78130 00821','98453 94494','01-09-2016 07:31:20','1560']]
	
	assert(extractCallsByBangalore(records) == [['(080)45291968','90365 06212','01-09-2016 06:30:36','9']] )
	print("Congratulations! Your extractCallsByBangalore")


testPartB()

calling_by_Bangalore = extractCallsByBangalore(calls)
count = 0

for item in calling_by_Bangalore:
	if extractPrefixesCodes(item[1]) == '(080)':
		count += 1

print("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(count/len(calling_by_Bangalore)))
