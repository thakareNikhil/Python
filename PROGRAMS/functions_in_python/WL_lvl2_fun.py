print('1] Accept string and separate words and find their length and reverse the string and print?' )
def S():
    return input('Entre String: ').split()
def L():
    a=S()
    for i in a:
        print(f'Word is {i}, length is {len(i)}')
    for i in a[::-1]:
        print(i[::-1],end=' ')

L()
print('Complete'.center(50,'='))


print('Accept a string and Find vowel contain words and consonant contain words ?')
def s():
    return input('Entre String: ').split()
def l():
    a=s()
    b='AEIOUaeiou'
    for i in a:
        c=True
        for k in b:
            if k in i:
                print(i,'= Vowel Word')
                c=False
                break
        else:
            if c:
                print(i,'= Consonant Word')
l()

