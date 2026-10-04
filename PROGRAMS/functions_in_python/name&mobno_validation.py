def name():
    while True:
        a=input('Entre your name :')
        if a.isdigit():
            print('Not allowed digits')
        else:
            b=a.split()
            c=True
            if a.isspace():
                print('Not allowed spaces')
            else:
                for i in b:
                    if not i.isalpha():
                        print('Invalid name ')
                        c=False
                        break
                else:
                    if c:
                        print('Your Name is Valid :',' '.join(b))
                        break
def No():
    while True:
        try:
            a = int(input('Entre Your Mobile no :'))
            if a in range(7000000000,10000000000):
                print('Valid mob no: ',a)
                break
            else:
                print('Invalid Mobile no')
        except ValueError:
            print('Invalid no.')

name()
No()