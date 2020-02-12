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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def isReceiveIncomingCalls( outgoingCall, records):	
	for item in records:
		incomingCall = item[1]
		if outgoingCall == incomingCall:
			return True
	return False

def isSendOrReceiveTexts( outgoingCall, records):
	for item in records:
		if outgoingCall == item[0] or outgoingCall == item[1] :
			return True
	return False

def test():
	records = [['78130 00821','98453 94494','01-09-2016 06:01:12','186'],
				['78298 91466','(022)28952819','01-09-2016 06:01:59','2093'],
				['97424 22395','78298 91466','01-09-2016 06:03:51','1975']]
	
	assert(isReceiveIncomingCalls('00000 00000',records) == False)
	assert(isReceiveIncomingCalls('78298 91466',records) == True)
	print("Congratulations! Your isReceiveIncomingCalls")


	texts = [['97424 22395','90365 06212','01-09-2016 06:03:22'],
				['94489 72078','92415 91418','01-09-2016 06:05:35'],
				['81520 43406','92421 64236','01-09-2016 06:09:34']]
	assert(isSendOrReceiveTexts('00000 00000',texts) == False)
	assert(isSendOrReceiveTexts('97424 22395',texts) == True)
	print("Congratulations! Your isSendOrReceiveTexts")

test()

telemarketers = []

for item in calls:
	if not isReceiveIncomingCalls(item[0], calls):
		if not isSendOrReceiveTexts(item[0], texts):
			telemarketers.append(item[0])

print("These numbers could be telemarketers: ",*sorted(set(telemarketers)), sep = '\n')






