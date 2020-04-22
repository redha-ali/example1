start = int(input("Enter start: "))
end = int(input("Enter End: "))

for x in range (start,end+1):
        for y in range (1,11):
            print (x,' * ',y, " = ",x*y)
        print ('------------------')