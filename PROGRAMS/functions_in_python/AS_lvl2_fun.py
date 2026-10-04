print('1] Find sum and avg of elements between list using 1 function call only')
def lst():
    a=int(input('Entre a range of list :'))
    b=[]
    if a<=0:
        return b
    else:
        for i in range(a):
            c=int(input(f'enter a number {i+1} :'))
            b.append(c)
        return b
def SA():
    a=lst()
    if len(a)==0:
        return 'List is empty'
    else:
        b=0
        for i in a:
           b=b+i
        return f'List: {a}',f'Sum: {b}',f'Avg :{b/len(a)}'
def P():
    res=SA()
    if type(res)==str:
        print(res)
    else:
        print(res[0])
        print(res[1])
        print(res[2])

P()
print('Complete'.center(50,'='))
