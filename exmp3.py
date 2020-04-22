class Game:
    def __init__(self):
        print ('Welcome in my Full Game')
        print ('Enter [1]','Enter [2]','Enter [3]',sep='\n')

        self.user_choices()

    def user_choices(self):
        while True:
            user_input = input("Enter your choice: ")
            print(type(user_input))

            try:
                user_input = int (user_input)

                if user_input == 1 :
                    print ("even odd game")
                    self.even_odd()
                elif user_input == 2 :
                    print ('sum avg game')
                    self.sum_avg()
                elif user_input == 3 :
                    print ('multi game')
                    self.mull_table()
                else :
                    print ('enter number between 1 & 3')

            except ValueError:
                print ('please enter valid number')

    def even_odd(self):
        print ('Tell me a number & I;ll tell you its type: ')
        while True:
            numb = input("Enter your number: ")

            if numb == "x":
                print('bye bye')
                break
                # exit()
            try:
                numb = int(numb)
                if numb % 2 == 0:
                    print(" even number")
                else:
                    print(" odd number")
            except ValueError:
                print("enter valid number")
            print('-------------------------------')

    def sum_avg(self):
        print('enters numbers to get sum')
        count = int(input('how many numbers you will sum: '))
        circle = 0
        sum = 0
        while circle < count:
            x = float(input('Enter number: '))
            sum += x
            circle += 1
        print('Sum is: ', sum)

    def mull_table(self):
        print ('Multiplication table')
        start = int(input("Enter start: "))
        end = int(input("Enter End: "))

        for x in range(start, end + 1):
            for y in range(1, 11):
                print(x, ' * ', y, " = ", x * y)
            print('------------------')

game1 = Game()