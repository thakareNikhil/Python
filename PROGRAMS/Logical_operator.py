#Logical operator comparison between two or more literals same or different data types also
#There are three type logical operator in python 'and','or','not'.
#That operator use for solving logical expression
#That operators gives result in define data types literals
#If We define bool value so its give True or False
#If We define str value so its give str output
#If We define int value so its give int output
#That operator is internally use True and False values in intgeral logical expression but give intgeral value
#That operator is internally use True and False values in str logical expression using length of str. but give str value
#That operator is internally use True and False values in bool using True=1 and False=0 logical expression but give bool value
a=int(input('Enter No1:'))
b=int(input('Enter No2:'))
c=input('Enter Str1:')
d=input('Enter Str2:')
# The 'and' operator do the product(Multiply) PVM of Two or more literals using True=>=1 and False=0
# The 'and' operator do the product(Multiply) PVM of Two or more str or int literals using length True=>=1 and False=0
# That operator after find False value it's not Run and result False value in his datatype
print('Ans Int:',a and b)#If a>=1 so PVM define as True and b==0 so it's define False and output b
print('Ans Str:',c and d)#If len(c)>=1 so PVM define as True and len(b)==0 so it's define False and output b or '' empty space
print('Ans Bool:',True and False)#True=1 ,False=0, 1*0==0 and 0=False ,the output is False
print('Ans Bool:',False and True)#True=1 ,False=0, 1*0==0 and 0=False ,the output is False
print('Ans Bool:',False and False)#True=1 ,False=0, 1*0==0 and 0=False ,the output is False
print('Ans Bool:',True and True)#True=1 ,True=, 1*1==1 and 1=True ,the output is True
print('='*50)
print('Ans Int:',10 and 0)#If a>=1 so PVM define as True and b==0 so it's define False and output b
print('Ans Str:','HI' and '')#If len("HI")>=1 so PVM define as True and len('')==0 so it's define False and output b or '' empty space
print('Ans Bool:',True and 0 and 'Python' and '')#True=1==T , 0==False => When he get False value it stop and give false val==0
print('Ans Bool:',True and 'True' and 'Python' and 12)#True=1 ,len('True')==<=1,len('Python')==<=1,12==<=1 output is True Because all Values are True
print('or'*50)
# The 'or' operator do the Sum PVM of Two or more literals using True=>=1 and False=0
# The 'or' operator do the Sum PVM of Two or more len(str) or int literals using length True=>=1 and False=0
# That operator after find True value it's not Run and result True value in his datatype
print('Ans Int:',a or b)#If a>=1 so PVM define as True and b==0 so it's define True and output a
print('Ans Str:',c or d)#If len(c)>=1 so PVM define as True and len(b)==0 so it's define True and output c
print('Ans Bool:',True or False)#True=1 ,False=0, 1+0==1 and 1=True ,the output is True
print('Ans Bool:',False or True)#True=1 ,False=0, 1+0==1 and 1=True ,the output is True
print('Ans Bool:',False or False)#False=1 ,False=0, 0+0==0 and 0=False ,the output is False
print('Ans Bool:',True or True)#True=1 ,True=, 1+1==2 and 2=True ,the output is True
print('='*50)
print('Ans Int:',10 or 100)#If 10>=1 so PVM define as True and 0==0 so it's define True and output 10
print('Ans Str:','HI' or '')#If len('HI')>=1 so PVM define as True and len('')==0 so it's define True and output 'HI'
print('Ans Str:','HI' or 200)#If len('HI')>=1 so PVM define as True output is 'HI'
print('Ans Str:',2 or 'HI')#If 2>=1 so PVM define as True output is 2
print('Ans Bool:',True or 0 or 'Python' or '')#True=1==T , 0==False => When he get True value it stop and give True val==True
print('Ans Bool:',True or 'True' or 'Python' or 12)#True=1 ,len('True')==<=1,len('Python')==<=1,12==<=1 output is True Because all Values are True
print('not'*50)
# The 'not' is the type of logical operator that output result only in True or False and applicable on only one literal
# The 'not' output the result of opposite the literal means literal True so it output False.
print('ANS:',not 'a')#The PVM use length of str literal  it's >=1 so it's define True but 'not' type operator result opposite Means False
print('ANS:',not '')#the str length is '0' means its False so 'not' operator shows the opposite of value means True
print('ANS:',not 1)#It's also same 1=True but 'not' give False
print('ANS:',not 12)#It's also same 12=True but 'not' give False
print('ANS:',not 0)#It's also same 0=False but 'not' give True
#we can't use literal before 'not' operator '1 not' without using 'and' & 'or' type operator '1 and not 3' or ' 2 or not 0 'if Literal two or more
#we can't use 'and' & 'or' direct after 'not' operator without define a literal 'not and','not or' its shows syntax error
print('USE 3 TYPES OF OPERATOR IN ONE:',True and 1 or False and 2 and 0  or not 5 and  False or 'TRUE' or 0 and 5 and not 3)# IT'S CORRECT
#print(True and 1 or False and 2 and 0  or not 5 not and  False or 'TRUE' or 0 not and 5 and not 3)# IT'S INCORRECT,Syntax error
'''
*ONE or MORE RelExpr diff DType
                 RelExpr1	RelExpr2	RelExpr1 and RelExpr2
				---------------------------------------------------------------------------------
					True	x	False	=		False		
	and				False	x	True	=		False
					False	x	False	=		False
					True	x	True	=		True
				-------------------------------------------------------------------------------
'''
'''
*ONE or MORE RelExpr diff DType
                    RelExpr1	RelExpr2	RelExpr1 or RelExpr2
				---------------------------------------------------------------------------------
					True	+	False	=		True			
	or				False	+	True	=		True		
					False	+	False	=		False	
					True	+	True	=		True
				---------------------------------------------------------------------------------
'''

'''
*Only one RelExpr solve at a Time
                    RelExpr1	Ans
                    not False	=   True
           not
                    not True	=   False	
'''