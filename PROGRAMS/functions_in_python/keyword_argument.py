"""3)keyword argument:These argument is use that time when user don't know the order of
 the formal parameters, but he knows the name of the formal parameters and which types input they hold or store
"""
def student_info(first_name,last_name,course,city):
    print(f'\t{first_name}\t\t{last_name}\t\t{course} \t{city}')
print('\tfirst_name\tlast_name\tcourse \tcity')
student_info(last_name='THAKARE',city='HYD',first_name='NIKHIL',course='PYTHON')
student_info('NIKHIL',course='PYTHON',last_name='THAKARE',city='HYD')

#==>If I input values in function call and define these values in formal parameters names so it's called keyword arguments its
#help to input values in same order, but we can define keyword argument before positional argument it gives syntax error

#student_info('NIKHIL',course='PYTHON',last_name='THAKARE','HYD') ==>it gives syntax error because we define keyword argument before
#positional argument so PVM gives first priority to positional argument and positional arguments follows the keyword argument
