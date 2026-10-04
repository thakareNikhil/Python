#The purpose of continue statement is to escape the value define in statement and print other
#'continue' is keyword
#The continue statement is use define inside the loop but this outdated
print('1]I will accept a string and escape the vowel char i string and print other and make list of vowels ')
a=input('Entre The String:')
b=[]
for i in a:
    if i.lower() in 'aeiou':
        b.append(i)
        continue
    print(i)
else:
    print(b)
print('COMPLETE'.center(15,'='))
print('2]It will accept integer and divide no 1 to n prime and not prime ')
a=int(input('enter the integer:'))
b=[]
if a<=0:
    print('Input Valid Range')
else:
    for i in range(1,a+1):
            if a%i==0:
                b.append(i)
                continue
print('Prime' if len(b)==2 else 'Not Prime')
print('COMPLETE'.center(15,'='))
print('3]accept list and remove negative element from list')
a=list(map(int,input('enter the list:').split()))
for i in a:
    if i<0:
        continue
    print(i)