import csv
import logging

#filler information for output, in list dict format
names = [
    {"fName": "Joe", "lName": "Mama", "occupation": "driver", "ID": "123456"},
    {"fName": "Roger", "lName": "Van Scoy", "occupation": "admin", "ID": "654321"},
]


with open('test.csv', mode='w') as csvfile:
    #headers
    fieldnames = ['fName', 'lName', 'occupation', 'ID']

    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    
    #iterates through each item in names
    for i in names:
        writer.writerow(i)

# create log
lgr = logging.getLogger('logger name')

lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG

# add a file handler
fh = logging.FileHandler('logTest.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)

# add the Handler to the logger
lgr.addHandler(fh)

# debug msg
lgr.debug('Debug notice')

#info msg
lgr.info('Info notice')

#warning
lgr.warning('Waning notice')

#error
lgr.error('Error')

#critical
lgr.critical('Critical message')