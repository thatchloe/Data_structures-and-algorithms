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



#Part A

area_code = []
for record in calls:
    number = record[0]
    
    if number[0] == '(':
        a_code = number[0:number.find(')')+1][:]
        if not a_code in area_code:
            area_code.append(a_code)
    
    elif number[0] in ['7','8','9']:
        mobile_code = number[0:number.find(' ')][:]
        if not mobile_code in area_code:
            area_code.append(mobile_code)
    
    elif number[0] == '140' :
        if not '140' in area_code:
            area_code.append('140')

print("The numbers called by people in Bangalore have codes:")

for code in sorted(area_code):
    print(code)


#Part B

count = 0 
for record in calls:
    call_num = record[0]
    rec_num = record[1]
    if call_num.startswith('(') and rec_num.startswith('('):
        call_code = call_num[0:number.find(')')+1][:]
        rec_code = rec_num[0:number.find(')')+1][:]
        if call_code == rec_code:
            count += 1
print(f"{round(float(count/len(calls)), 2)*100} percent of calls from fixed lines in Bangalore are calls\nto other fixed lines in Bangalore")
        
        
