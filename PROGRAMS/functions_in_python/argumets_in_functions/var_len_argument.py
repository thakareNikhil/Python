"""4)pure Variable length argument: This argument PVM treated as positional argument but this argument we can define after the positional
argument ,this argument treated as formal parameter length argument it holds the <class:'tuple'> inputs ,it allows duplicates,
str,complex,float,int etc. by following tuple immutability we can give multiple input by using this argument it defines in 
function definition as a formal parameter length argument by using '*formal parameter name'
the variable length argument is holding multiple inputs not require to define multiple formal parameter in function definition for
holding multiple inputs only define '*parameter name' and it holds the multiple inputs
it's less the function code duplication
If we are not defined formal parameter length argument so it holds only specific values or inputs, and we can entre only specific length of
inputs only if user want to entre multiple inputs but we don't how many values user input in function call so for that we require lot
of formal parameter define in function definition and its make lot of function duplication code means 1000function calling 1000function
definition required for defend that type of situation the variable length argument is defined in functions
print() follows this argument internally
"""
print('Variable length argument ')
print('Without variable length argument')
def emplist1(emp1,emp2,emp3,emp4):#==>emp1,emp2,emp3,emp4:are positional formal parameters
    print(emp1,emp2,emp3,emp4)
emplist1('nt','vt','st','mp')#==>its positional arguments for team of 4 emp only

def emplist2(emp1,emp2,emp3):#==>emp1,emp2,emp3:are positional formal parameters
    print(emp1,emp2,emp3)
emplist2('nt','vt','st')#==>its positional arguments for team of 3 emp only

def emplist3(emp1,emp2):#==>emp1,emp2:are positional formal parameters
    print(emp1,emp2)
emplist3('nt','vt')#==>its positional arguments for team of 2 emp only

def emplist4(emp1):#==>emp1:are positional formal parameters
    print(emp1)
emplist4('nt')#==>its positional arguments for team of 1 emp only

def emplist5():
    print()
emplist5()#==>its positional arguments for team of 0 emp only
print('='*100)

print('With variable length argument')
def emplist1(*emp):#==>*emp:are formal parameters length argument
    print(emp)
    print(type(emp))
emplist1('nt','vt','st','mp')#==>its positional arguments for team of 4 emp hold by variable length argument
emplist1('nt','vt','st')#==>its positional arguments for team of 3 emp hold by variable length argument
emplist1('nt','vt')#==>its positional arguments for team of 2 emp hold by variable length argument
emplist1('nt')#==>its positional arguments for team of 1 emp hold by variable length argument
emplist1()#==>its positional arguments for team of 0 emp hold by variable length argument
emplist1(23,'nikhil','python',True,2+5j)#we can store any type of data because its tuple class

def emplist2(*emp,sname):pass#==>it's give syntax error because first we defined variable length argument and its tuple object
#tuple store multiple data it's not limit so any type of input entre by user it holds '*emp' and 'sname' is empty always so for that
#it's give syntax error it allows to define after positional argument because PVM gives the high priority to positional arguments