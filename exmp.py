
while True:
    numb = input("Enter your number: ")

    if numb == "x" :
        print ('bye bye')
        break
        #exit()

    try :
        numb = int (numb)
        if numb % 2 == 0:
            print(" even number")
        else:
            print(" odd number")
    except ValueError:
                print("enter valid number")
    print ('-------------------------------')