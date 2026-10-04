#String is the datatype that store set of Alphanumeric,integer,special symbols data
#Any type of data input in single,double quotes and single,double triple quotes is called as string data type
#str datatype is immutable that not allow to change and modify value at same id
#There are 23 predefined function that use for modify or change or print modified string on different id
#=>title(),capitalize(),upper(),lower(),swapcase(),count(),index(),find(),replace(),center(),split(),join(),lstrip(),rstrip(),strip(),endswith(),startswith(),__contain__(),isupper(),islower(), isspace(),isalpha(),isdigit(),isalnu()

a='    1  mY name Is nIkhIL Thakare 2004 mY AGE 22  1   '
b='    {12132}    '
c='22 Nikhil-thakare '
d=' '
e=['a','b','c','d']
f='ABC12'
g='abc'
A='12342'
print('\ttitle() ==>',a.title())#the title function print each word first letter uppercase in str not change numbers.
print('\ttitle() ==>',b.title())
print('\tcapitalize() ==>',a.capitalize())#the capitalize function print 1st word first letter uppercase only in str not change numbers.
print('\tcapitalize() ==>',b.capitalize())
print('\tupper() ==>',a.upper())#the upper function print uppercase str not change numbers
print('\tlower() ==>',b.lower())#the lower function print lowercase str not change numbers
print('\tswapcase() ==>',a.swapcase())#the swapcase function swap case of letters ,upper into lower and lower into upper. not change numbers
print('\tcount() ==>',a.count('a'))#the count function count the given substring or chr or anything in quotes how many times are in string object count and give no.
print('\tcount() ==>',a.count('mY'))
print('\tindex() ==>',a.index('I'))#the index function give the index no of the given substring or chr or anything in quotes in string object
print('\tindex() ==>',a.index('mY'))
print('\tfind() ==>',a.find('I'))#the find function give the index no of the given substring or chr or anything in quotes in string object
print('\tfind() ==>',a.find('mY'))#is outdated is work like index() but if value is not str obj it gives -1 index but index give value error
print('\treplace()==>',c.replace(' ','*'))#the replace function is replace the given values by user in str obj by given values in replace function
print('\treplace()==>',c.replace('kh','**'))
print('\tcenter()==>',c.center(100,'*'))#it prints the str obj in center and add the value in ends() and starts() str obj define in center()
print('\tsplit()==>',a.split())#split function is make a list of given string and separate the words by comma using by default space ' ' in str obj
print('\tsplit()==>',c.split('-'))# if you give delimiter in split function so it separate the words from that
print('\tjoin()==>',d.join(e))# that function join the list data or elements and make separate the elements by given str in join function or define in join function make string
print('\tjoin()==>','*'.join(e))
print('\tlstrip()==>',a.lstrip())#it removes left side space unused spaces or value give in strip function and print string
print('\tlstrip()==>',a.lstrip('1'))
print('\trstrip()==>',a.rstrip())#it removes right side space unused spaces or value give in strip function and print string
print('\trstrip()==>',c.rstrip('22'))
print('\tstrip()==>',b.strip())#it removes both side space unused spaces or value give in strip function and print string
print('\tstrip()==>',b.strip('{}'))
#that function give bool value True or False
print('\tendswith()==>',c.endswith('re '))#it checks given values in endswith function at the end of in str obj and give True or False
print('\tendswith()==>',c.endswith('re'))
print('\tstartswith()==>',c.startswith('22'))#it checks given values in startswith function at the start of in str obj and give True or False
print('\tstartswith()==>',c.startswith('Nikhil'))
print('\t__contain__()==>',c.__contains__('2004'))#it checks given values in __contain__ function are in str obj or not and give True or False
print('\t__contain__()==>',c.__contains__('2005'))
print('\tisupper()==>',f.isupper())#it checks the full str obj in uppercase
print('\tislower()==>',g.islower())#it checks the full str obj in lowercase
print('\tisspace()==>',d.isspace())#it checks the str obj contain only spaces
print('\tisalpha()==>',f.isalpha())#it checks the str obj contain only alphabets not space or not no or not special symbal
print('\tisdigit()==>',A.isdigit())#it checks the str obj contain only digits not space or not char or not special symbal or not float point
print('\tisalnum()==>',f.isalnum())#it checks the str obj contain only alphabets or digits not space or not special symbal or not float point
