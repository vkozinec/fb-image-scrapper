import csv
import urllib.request
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('disu.txt') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list based on column name k

strings = columns['status_link'] # take only status_link column out of list

# loop and remove any of '' empty values inside list if any exists. This is to avoid errors in further loop if there is no url to download.
while True:
  try:
    strings.remove("")
  except ValueError:
    break

# split list value ( it's always the same URL ), and take only img ID from url 
strings = [i.rsplit('/', 2)[-2] for i in strings]

# fint length of list, so we can loop trough all values
sumtotal = len(strings)
count = 0

#while (count < sumtotal-1):    this is "while" for automatic loop based on list length, now we just take few elements to test
# enumerate returns sequence number for each iteration
# string[:20] gets the first 20 elements. This is called slicing*
for count, one in enumerate(strings[:20]):
    one = one.rsplit('/', 1)[-1]
    newurl = ('https://graph.facebook.com/'+ one +'/picture')
 
    try:
        urllib.request.urlretrieve(newurl, 'slike/test{}.jpg'.format(str(count)))
        print(newurl, "Downloaded")
    except Exception as e:
        print(type(e))
        print(inst.e)
        print(e)