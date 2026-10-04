#2)Default Parameter:These arguments is use for passing same or default value for all time by function calling
#some arguments  are already define in function definition or function heading or formal parameters
#if user not input value on default argument so python print by default consider default value define in function heading or function definition
#Default argument mechanism
def student_info(first_name,last_name,course,city='HYD'):#==>'city':is the default parameter or argument or both that print by holding default value if user not entre any argument at 4th position so its consider by default 'HYD'
    print(f'\t{first_name}\t\t{last_name}\t\t{course}\t{city}')
print('\tfirst_name\tlast_name\tcourse\tcity')
student_info('Nikhil','Thakare','Python')
student_info('Nikhil','Thakare','Python','USA')

#def student_info2(first_name,last_name,course='python',city):
#'course':is the default parameter or argument or both that holding default value
#but is giving syntax error because PVM gives first priority to positional argument and 'course' is default argument that define before
#positional argument so it's giving error
#we  can pass any type of argument after the positional arguments only and default arguments pass or define at last position only in function definition
