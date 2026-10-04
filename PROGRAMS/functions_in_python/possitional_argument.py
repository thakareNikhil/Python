#1)positional argument:This argument is use PVM by default in all function PVM gives first priority to this argument
#the positional arguments mechanism is default argument passing mechanism
#maintain the order for passing values in formal parameters ,user should know the order of parameters define in
#function if we don't know so the values order will be disturbed and output is not correct
#Positional argument mechanism
def student_info(sr_no,name,course,city):#==>sr_no,name,course,city :these are called formal parameters define in function heading
    print('\t\t{}\t{}\t{}\t{}'.format(sr_no,name,course,city))
print('\tsr_no\tname\tcourse\tcity')
student_info(1,'Nikhil','Python','HYD')#==>1,'Nikhil','Python','HYD' :These are called arguments or inputs passes in order in formal parameters
student_info('Dany',1,'USA','C++')#==>1,'Dany',1,'USA','C++':These are called arguments or inputs passes in unorder format
# and it's disturbing the output, and it's order means values is not passes or input by formal parameters order
# formal parameters hold the unordered value passing by arguments and store data in their datatypes because python is dynamic typed programming language


