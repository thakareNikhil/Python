def emp(s_no,name,salary,*skills,city='HYD',**info):
    """'s_no','name','salary': are positional arguments ,*skills:is variable length argument parameter
    'city': is default parameter ,'**family ' :is keyword variable length argument parameter
    if keyword variable length parameter ar not define in function but default argument defines so its position is last always
    else before keyword variable length parameter argument"""
    print(f'{s_no}.Employee_name :{name} City :{city}')
    print(f'Salary is :{salary}')
    print(f'skills :{skills}')
    print('=' * 50)
    for k,v in info.items():
        print(f'{k} of {v}')
    print('=' * 50)
emp(1,'SK',120000,'c++','python','linux','html','css','java',father='MK',brother='DK',mother='YK')
emp(2,'NIKHIL',1000000,'c++','python','linux','html','css','JS','numpy','pandas','Django','SQL','English',father='KT',mother='MT')
emp(3,'SK',1200)
emp(4,'VT',1000000,city='Nagpur',owner='Unirova',turnover=10000000000000)