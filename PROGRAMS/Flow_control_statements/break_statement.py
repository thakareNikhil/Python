#The purpose of break statement to break is that it use in only looping statements
#user define any conditional statement in loop so break statement is in use mostly
#if condition is false so the break statement is run exit from the loop and execute else or other statement part
#the 'break' statement is logical exit means is exit from only loop and execute other statement or else block
#The 'break' is a keyword
print('1] It will accept a integer check it is prime or not')
a=int(input('enter the number:'))
b='Prime'
#prime no. is always start from 2
if a<=1:
    print('Enter a >=2 integer:')
for i in range(2,a):
    if a%i==0:
        b=' Not Prime'
    break
print('The No.{} is {}'.format(a,b))
print('COMPLETE'.center(15,'='))
print('2]It will accept a String and print this to index define by user ')
a=input('enter the string:')
b=int(input('enter the index u want print upto:'))
for i in a:
    if a[b]==i:
        break
    print(i)
print('COMPLETE'.center(15,'='))
print('''3]It will check if string enter by user is contain vowel or not
        if it contain so print this string upto before vowel char''')
a=input('enter the string:')
b='AEIOUaeiou'
for i in a:
    if i in b:
        break
    print(i, end='')
print('COMPLETE'.center(15,'='))
print('4] It will Check the list all no. are +Ve or not If Not so it stop printing the elements')
a=list(map(int,input('enter List:').split()))
for i in a:
    if i<0:
        print('Negative')
        break
    else:
        print(i)