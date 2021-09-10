str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = '123'
#str3 = str3 +1

x = int(str3) + 1
print(x)


#name = input('Enter:')
#Enter:Chuck
#print(name)
#apple = input('Enter:')
#Enter: 100
#x = apple - 10
#x = int(apple) - 10
#print(x)


fruit = 'banana'
letter = fruit[1]
print(letter)
#a
x=3
w=fruit[x-1]
print(w)
#n

zot = 'abc'
#print(zot[5])

fruit = 'banana'
x = len(fruit)
print(x)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


fruit = 'banana'
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

