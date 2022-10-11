a=open("simpsons_phone_book.txt","r")
for phoneno in a:
    if (re.search(r'^J\w*\s*(Neu)', phoneno)):
        print(phoneno)
a.close()
c = print(a.read())
import re
h = re.findall("Neu$*[0-9]{3}-[0-9]{4}",a.read())
print(re.findall("^J\w*Neu$\d{3}-\d{4}",a.read()))

e = re.compile(r'^J')
e.findall(a.

          
import re
fh = open("simpsons_phone_book.txt", 'r')

for line in fh:
    if (re.search(r'^J\w*\s*(Neu)', line)):
        print (line)


fh.close()

#mini task 2

a=open("largest_cities_germany.txt",'r')
b=open("postal_codes_germany.txt",'r')
largest_cities=a.readlines()     #to read in list form
regex_cities=re.search(\s[\w\s]+\s+)
































