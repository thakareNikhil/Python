#The ternary if else operator is operation performing like if else statement but difference in both
print('1]Write a program to find the greater of two numbers using the if..else operator.')
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=a if a>b else b if b>a else 'Both are equal'
print('greater no {} {}==>{}'.format(a,b,c))
print('2]Write a program to find the smaller of two numbers using the if..else operator.')
c=a if a<b else b if b<a else 'Both are equal'
print('smaller no {} {}==>{}'.format(a,b,c))
print('3]Write a program to check whether a number is even or odd using the if..else operator.')
c='Even' if a%2==0 else 'Odd'
print('{} is ==>{}'.format(a,c))
print('4]Write a program to check whether a number is positive or negative using the if..else operator.')
c='POSITIVE' if a>0 else 'NEGATIVE' if  a<0 else 'ZERO'
print('{} is ==>{}'.format(a,c))
print('5]Write a program to check whether a person is eligible to vote based on age using the if..else operator.')
A=int(input('ENTER AGE:'))
c= 'YOU CAN VOTE' if A>=18 else 'YOU CAN NOT VOTE'
print('Vote eligibility {}=={}'.format(A,c))
print('6]Write a program to determine whether a student has passed or failed based on marks using the if..else operator.')
M=int(input('ENTER MARKS:'))
c= 'Pass' if M>=40 else 'Fail'
print(f'YOU ARE {c}')
print('7]Write a program to calculate the grade of a student (A, B, C, or F) using nested if..else operators.')
a=int(input('\tMATH: '))
b=int(input('\tMARATHI: '))
c=int(input('\tHINDI: '))
D=(a+b+c)/3
A='A' if D>=80 else 'B' if D>=60 else 'C' if D>=40 else'Fail'
print(f'YOUR GRADE IS==> {D}')
print('8]Write a program to find the largest of three numbers using nested if..else operators.')
d=a if a>b and a>c else b if b>a and b>c else c if c>a and c>b else 'EQUAL' if a==b==c else ''
print(f'THE GREATER NO IS :{d}')
print('9]Write a program to find the absolute value of a number using the if..else operator.')
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=a if a>0 else b if b>0 else a,'and',b if a==b and a>0 else 'zero'
print(f'THE ABSOLUTE VALUE FROM BOTH :{c}')
print('10]Write a program to check whether a given year is a leap year using the if..else operator')
a=int(input('Enter a year: '))
b='Leap Year' if a%4==0 and a%100!=0 or a%400==0 else 'Not Leap Year'
print(f'This is {b}')
print('11]Write a program to check whether a character is a vowel or a consonant using the if..else operator.')
a=input('ENTER Char:')
b='AEIOUaeiou'
c= 'VOWEL' if a in b else 'CONSONANT'
print(f'This is {c}')
print('12]Write a program to check whether a given character is an alphabet or not using the if..else operator.')
a=input('ENTER Word:')
b='!@#$%^&*'
c= 'Digit' if a.isdigit() else 'special character' if a in b else 'ALPHABET'
print(f'This is {c}')
print('13]Write a program to check whether a character is uppercase or lowercase using the if..else operator.')
a=input('ENTER Word:')
b='Uppercase' if a==a.upper() else 'Lowercase'
print(f'This is {b}')
print('14]Write a program to check whether a number is divisible by both 3 and 5 using the if..else operator.')
a=int(input('Enter a number: '))
b= 'YES' if a%3==0 and a%5==0 else 'NO'
print(f'{b}')
print('15]Write a program to determine whether a number is a single-digit number or a multi-digit number using the if..else operator.')
b='Singal Digit ' if a in range(0,10) else 'Two Digit 'if a in range(10,100) else 'Multidigit'
print(f'NO IS =>>{b}')
print('16]Write a program to determine whether a business transaction results in profit or loss using the if..else operator.')
a=100
b=float(input('MRP:'))
c=f'Profit :₹{b-a}' if b>a else f'Loss :₹{a-b}'
print(f'{c}')
print('Write a program to determine whether a person can enter a movie theater based on the age restriction using the if..else operator.')
a=int(input('Enter a person age: '))
b= 'WELCOME' if a>12 else 'NOT allow'
print(f'YOU ARE {b}')