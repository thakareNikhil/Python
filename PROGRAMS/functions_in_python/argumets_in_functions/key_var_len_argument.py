"""5)Keyword variable length argument :This argument treated as keyword variable length parameter argument denoted '**parameter_name'
in function definition part ,The keyword variable length parameter argument is the object of <class:'dict'> it holds key
and values it not allow duplicates keys, but allow duplicate values and multiple keys&values its follows all fundamentals of dict datatype class
It define in function definition part at the last position of all arguments because if we denoted before default argument it holds the default argument values also in dict object
and default argument is empty so its give syntax error
This parameter works like variable length parameter it reduces the code duplication , it reduces the time but deference is variable length parameter argument
holds the tuple class inputs and keyword variable length parameter argument holds the dict class key and values
if we don't know user enters how many inputs and which name (formal parameter) gives to this inputs that these argument is in used
if we not use these argument so we required 1000 no.of function definition for 1000 function calls and it increases the code duplication
so for reducing the function definition part means define only one function definition with keyword variable length parameter argument
and we call multiple times function in program for that situation it used
"""
print('Without keyword variable length argument')
def student(sname,std,math,marathi,hindi,english):#==>sname,std,math,marathi,hindi,english: those are positional arguments with fix length for holds inputs
    print(sname,std,math,marathi,hindi,english)
student('SK',math=12,hindi=100,marathi=91,std='XII',english=100)#==>we give only limited inputs define in function body means
#I want adds some other subject marks with their name so its give syntax error or adds some different info by using different keyword argument name
#it's not possible because we won't define these name formal parameters in function definition part
def student(sname,std,math,marathi,hindi):
    print(sname,std,math,marathi,hindi)
student('MK','X',20,82,96)
def student(sname, income,scholarship=1000,totalfees=10000):#==>'scholarship','totalfees' :is default argument parameter
    print(sname,income,scholarship)
    print('fees required to pay :',totalfees-scholarship)
student('MK',50000)#==>at that time we store different info about student so we required to define different parameters
#in function definition part then student get input if student get input different so that type of situation we use keyword
#variable length argument means you don't know which type user input values which names it gives that time situation if we don't use
#it makes code complicated and increase code duplication

print('With keyword variable length argument')
def student1(**stuinfo):
    print('='*50)
    print(type(stuinfo),stuinfo)
    print('=' * 50)
    for k,v in stuinfo.items():
        print(f'{k} = {v}')
    print('=' * 50)

student1(name='MK',math=10,marathi=91,hindi=100,english=100)
student1(sport='kho-kho',date='12/03/2026',fees=120)
student1(cricket=50,kho_kho=30,football=200,badminton=20,running=0)
student1()
#you see above it reduces code duplication and not required to define formal parameters in function and not required to define function repeatedly
#it's not holds the limited input means user self define keys and values in function call part and, we can leave empty also

