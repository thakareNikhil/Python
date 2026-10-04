#The identity is not necessary to remember because it's not use mostly ,that operator is same as relational operator '==' and '!='.
#There are Two types of identity operator 'is' and 'is not' that use for compare the id() the value and gives True and False result
#the 'is' operator work same values means deep copy it gives True
#the 'is not' operator work difference values means shallow copy  it gives True
#the 'is' operator work difference values means deep copy it gives False
#the 'is not' operator work same values means shallow copy  it gives False
print( 2 is 1)#means 2==1 it gives false
print( 2 is not 1)#means 2!=1 it gives true
print( 2 is 2)#means 2==1 it gives true
print( 2 is not 2)#means 2!=1 it gives false
#it means is not compare values it compare id()
a=2
b=2
print(a is b)# it gives True because both id are same
print(id(b))
print(id(a))

