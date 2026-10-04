print('3] Name validation Program')
while True:
    a=input('Enter your name:')
    b=a.split()
    if a.isspace():
        print('Dont Entre only space')
    else:
        if len(b)==0:
            print('you Not Entre any thing "TRY AGAIN" ')
        else:
            c=True
            for i in b:
                if not i.isalpha():
                    c=False
                    break
            else:
                if c:
                    print('Your name is valid',' '.join(b))
                    break
                else:
                    print('Try Again')