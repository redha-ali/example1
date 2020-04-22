print ('enters numbers to get sum')
count = int(input('how many numbers you will sum: '))
circle = 0
sum = 0
while circle < count :
    x = float(input('Enter number: '))
    sum += x
    circle += 1
print ('Sum is: ',sum)