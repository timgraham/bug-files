import csv
import re

regex = re.compile(r'^[a-z][a-z0-9]+([-.+][a-z0-9]+)?\Z')

spamReader = csv.reader(open('uri-schemes-1.csv', newline=''))
for row in spamReader:
    if not regex.match(row[0]):
        print(row[0])
