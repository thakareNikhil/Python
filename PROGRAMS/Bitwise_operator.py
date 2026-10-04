#The Bitwise operator perform the operation on set data type and integer Data type only and perform operation bit by bit
#The bitwise operator are applicable on int no. only because float value is not certain value
#That operator covert data in binary form and store in main memory
#That gives data or result to user in decimal form because python is high level language
#There are six types of bitwise operator '<<':left shift,'>>':right shift,'|':bitwise or,'&':bitwise and,'~':compliment operator,'^':XOR operator
#THE LEFT '<<' AND RIGHT '>>' SHIFT BITWISE OPERATOR
print('<< =',12<<3)#the left shift operator the 12 is int value and 3 is a power of 2 that internally work in binary no.then it gives decimal no.
print('<< =',100<<100)#it gives you ANS 100*2**100==126765060022822940149670320537600
'''the formula for solving 12*(2**3)=96 for end-user but internally it give result by converting binary no to this integer and 3 bits in left side
and make new binary no then give the result in decimal form of this binary no.
for ex: 12 is int no that come in 4 bit range means 0 to 15 so 0b1100 is the binary form so 3 means 000 that shift to the
left side of 0b1100 this binary no means its convert as 0b1100+000 ==0b1100000 so it's convert into decimal form means 96
so that ans is 96 , that all thing depend on bit range or power of 2 ,if you give 4 power then it shift 0000 zeros on left side.
'''
print('>> =',12>>3)#the right shift operator the 12 is int value and 3 is a power of 2 that internally work in binary no.then it gives decimal no.
print('>> =',100>>100)#it gives you ANS: 100//(2**100)==0 use can apply flore division for getting ANS: using formula
print('>> =',12>>1)#it gives you ANS: 12//(2**1)==6 use can apply flore division for getting ANS: using formula and gives only int ans
'''the formula for solving 12//(2**3)=1 for end-user, but internally it give result by converting binary no to this integer and 3 bits in Right side from left end
and make new binary no then give the result in decimal form of this binary no.
for ex: 12 is int no that come in 4 bit range means 0 to 15 so 0b1100 is the binary form so 3 means 3 bit 100 means 000 from binary bin(12) that shift to the
left side of 0b1100 this binary no means its convert as 0b0001 ==0b0001 so it's convert into decimal form means 1
so that ans is 1 , that all thing depend on bit range or power of 2 ,if you give 4 power then it shift 0000 zeros on right side and ans is 0.
'''
#BITWISE OR'|' AND BITWISE AND '&' OPERATOR
print('| =',12|3)#its work internally bin(12)+bin(3)=int(bin((bool(ans))) covert bit by bit
print('| =',14|14)#0b1110 + 0b1110 = 0b1110 = 14
print('| =',12|0)#0b1100 + 0 = 0b1100 = 12
'''it convert both values in binary form and make addition and this addition ANS convert int(bool) bit by bit means like logical operator
if 0b1100 + 0b11=0b1111==15 int(bool) convert bit by bit and make a binary no and give result in decimal no.
IMP: the bitwise or'|' operator and logical 'or' operator are completely different because Logical 'or' operator have no restrictions
means it input all type of data and compare them str,list,float  but bitwise '|' operator have restrictions it input and compare only int and set data  
 0b1100
+0b0011
--------
 0b1111
'''
#the '|' operator and set function union() are same the union function use in set datatype is work on '|' operator
print('"|" in set=',{1,2,3,4}|{0,8,65,3}) #the bitwise '|' operator and set function union both are same
print('.union() in set=',{1,2,3,4}.union({0,8,65,3}))
print('& =',12|3)#its work internally bin(12)*bin(3)=int(bin((bool(ans))) covert bit by bit
print('& =',14|14)#0b1110 * 0b1110 = 0b1110 = 14
print('& =',12|0)#0b1100 * 0 = 0b1100 = 12
'''it convert both values in binary form and make Multiplication and this Multiplication ANS convert int(bool) bit by bit means like logical operator
if 0b1100 * 0b11=0b0000==0 int(bool) convert bit by bit and make a binary no and give result in decimal no.
IMP: the bitwise and '&' operator and logical 'and' operator are completely different because Logical 'and' operator have no restrictions
means it input all type of data and compare them str,list,float  but bitwise '&' operator have restrictions it input and compare only int and set data  
 0b1100
*0b0011
--------
 0b0000
'''
#the '&' operator and set function intersection() are same the intersection function use in set datatype is work on '&' operator
print('"&" in set=',{1,2,3,4}&{0,8,65,3}) #the bitwise '&' operator and set function intersection() both are same
print('.intersection() in set=',{1,2,3,4}.intersection({0,8,65,3}))
#The '|' and union() both are work on addition concept internally but different method using state value of element in set
#The '&' and intersection() both are work on multiplication concept internally but different method using state value of element in set
#BITWISE ''^':'XOR'(exclusive or operator) OPERATOR
print('^ =',10^10)#the both value convert in binary form if both bit are same so it give zero '0'
print('^ =',10^1)#the both values bit are difference it gives 1 and make 3rd binary and convert into decimal and give result
print('^ =',15^0)#It gives the same result 15 result
'''That operator covert both in to binary no and comparison on it using their bit ,if both values bits are same so it gives 0 zero 
but if both values bit difference it gives 1 one bin(10)=0b1010 SO 1 0 1 0
                                                                   1 0 1 0
                                                                ------------
                                                                   0 0 0 0   0b0000==0 so ANS is 0
ex:    value1    value2      value1^value2 
-----------------------------------------------      
       True      True        False
       False     False       False
       True      False       True
       False     True        True
2)we are also do swapping using 'XOR''^' operator 
a=10
b=2
a=a^b==0b1000==bin(8) a==8
b=a^b==0b1010==bin(10) b==10
a=a^b==0b0010==bin(2)  a==2
IT SWAP USING XOR operator '^'
3)The XOR ^ operator is the same of set function symmetric_difference() they both working and both are same,the set function symmetric_difference()
is work internally using XOR operator and give the difference from both set 
'''
a=10
b=20
print('value(a) :',a)
print('value(b):',a)
a=a^b
b=a^b
a=a^b
print('SWAP :',a)
print('SWAP :',b)
print('XOR in set'.center(50,'='))
x={1,2,3,4,5,6,7}
y={4,5,67,3,1,9}
z=x^y
w=x.symmetric_difference(y)
print('USING XOR:',z)
print('USING SET FUNCTION symmetric_difference():',w)
print('_x'*50)
#COMPLIMENT BITWISE OPERATOR '~'
print('~:',~10)# ~10=>-(10+1)==-11
print('~:',~-10)# ~-10=>-(-10+1)==9
print('~:',~0)# ~0=>-(0+1)==-1
print('~:',~-1)# ~-1=>-(-1+1)==0
'''That operator is gives positive and negative that depend on user input no ,if user input positive no, so it gives negative 
answer but user input negative value so it gives positive answer 
The formula for end-user solving the expression simply ~no--->-(no+1)==-no, ~-1-->-(-no+1)=no
The calculation rule of bit by bit in complement operator if sum 1 + 1 bit its ans is 0 with carry 1 and move forward
if the sum 0 + 0 bit its ans is 0
.'.But it internally hows solve that a point so if user any positive no so , first it convert into bin(+no) and add bin(1) then solve bit by bit
after he get ans so it convert in decimal form.
.'. But if user enter negative no so first it convert the bin(-no) then it inverted the this no means 1 is 0 and 0 is one
after he get inverted binary no the it add bin(1) after doing addition it get ans new binary no so it invert this ans double
and after invert it get a binary no so it convert into decimal form and give that ans means it follow 2S operation it means it 
do invertion or flip of no two times  

'''