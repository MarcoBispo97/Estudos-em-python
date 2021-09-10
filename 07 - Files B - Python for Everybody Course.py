xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count +1
print('Line Count:', count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startwith('From:')
        print(line)
        