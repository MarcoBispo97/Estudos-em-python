s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it!')


#word = input("Type banana")
word = 'banana'
if word == 'banana': 
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', come after banana.')
else:
    print('All right, bananas.')

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'. lower())


    #stuff = 'Hello world'
    #typer(stuff)
       #dir(stuff)
    #['capitalize', 'casefold', 'center', 'count', 'encode', 'endwith', 'expantabs']

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)

greet = '   Hello Bob   '
greet.lstrip()
greet.rstrip()
greet.strip()

#line = 'Please have a nice day'
#line.startwith('Please')
#line.startwith('p')

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('0')
print(atpos)
sppos = data.find('', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

word = 'banana'
i = word.find('na')
