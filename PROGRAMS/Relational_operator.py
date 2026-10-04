#Relational operator always do comparison between Two values or literals
#There are six types of Relational operator in python '>', '<', '==', '!=', '>=', '<='.
#That operator is use for solving relational expression
#That operators give the result in True and False means in bool Datatype
#relational Operator checks relational expression using only no. value if comparison between numbers so its compare given no.
#but given value is str so its check its order no and then compare.
a=int(input('Enter No1:'))
b=int(input('Enter No2:'))
c=input('Enter Str 1:')
d=input('Enter Str 2:')
print('ANS:',a<b)#it's less than type opr that compare between two Integers and check its True or False
print('ANS:',c<d)#it's greater than type opr that compare between two Integers and check its True or False
print('ANS:',a>b)#it's less than type opr that compare between two Str, Char chr() using its Order ord() No (it's internally process) and check its True or False
print('ANS:',c>d)#it's greater than type opr that compare between two Str, Char chr() using its Order ord() No (it's internally process) and check its True or False
# '>' and '<' in that type we can define same datatype values only and compare between
x=input('Enter Char1:')
y=input('Enter Char2:')
print('ORDER NO OF CHAR 1:',ord(x))#that function is use for getting order no (define in language internally) of char
print('ORDER NO OF CHAR 2:',ord(y))#using that order no the relational operator give output True or False in str values comparison
v=int(input('Enter no1:'))
w=int(input('Enter no2:'))
print('USE ORDER FOR GET CHAR :',chr(v))#that function is use for getting char using No.
print('USE ORDER FOR GET CHAR :',chr(w))
print('ANS:',a==b)#it's double equal to that's check the val1 is equal val2 and give output True and False
print('ANS:',a!=b)#it's not equal to that's check the val1 is not equal to val2 and give output True and False
print('ANS:',c==d)#it's double equal to that's check the str1 is equal str2 and give output True and False
print('ANS:',c!=d)#it's not equal to that's check the str1 is not equal to str2 and give output True and False
print('Diff DType:',a==d)
print('Diff DType:',a!=c)
# '==' and '!=' in that type we can define different datatypes values also and compare between
print('ANS:',a<=b)#it's less than equal to that's check the val1 is equal or less than val2 and give output True and False
print('ANS:',a>=b)#it's greater than equal to that's check the val1 is equal or greater than val2 and give output True and False
print('ANS:',c<=d)#it's less than equal to that's check the str1 is equal or less than str2 using order no  and give output True and False
print('ANS:',c>=d)#it's greater than equal to that's check the str1 is equal or greater than str2 using order no and give output True and False
# '>=' and '<=' in that type we can define same datatype values only and compare between if we use different datatypes literals it's trow type error
