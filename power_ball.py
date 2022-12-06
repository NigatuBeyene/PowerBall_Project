import random
#THIS POWER BALL PROJECT WORKING WITH OOP(OBJECT ORENTED PROGAMIGN)Run-time Polymorphism:

from colorama import Fore
print(Fore.LIGHTGREEN_EX, "\n\n DEVELOPER NAME:", Fore.RESET, Fore.LIGHTRED_EX, "NIGATU BEYENE", Fore.RESET)
print(Fore.YELLOW, "WELLOCOME TO POWERBALL LOTTERY WEBSITE \n", Fore.RESET)



class Win_number():
       # this Win_ number class program work for 5 random numbers and
       # power balls for mega million lottery Winner numbers

    def white_balls(self):             # five random numbers methoda/method for Win_numbers
        print(Fore.LIGHTCYAN_EX, "Today's Powerball Winning Numbers:", Fore.RESET)
        list1 = []                     # Empity list use for put random numbers
        self.list1 = list1
        for num1 in range(5):          # select only five numbers in 20 numbers
            r = random.randint(1, 20)  # random numbers limit values
            list1.append(r)            # append random number in to 'list1'
        list1.sort()                   # makes ascending order for all  'list1'
        print(Fore.LIGHTMAGENTA_EX, *list1, Fore.RESET,  end=" ")

    def power_ball1(self):  # Power ball methoda/methode for Winner numbers

        power1 = []
        for num1 in range(1):
            power1 = random.randint(1, 10)  # c
        self.power1 = power1
        print(Fore.LIGHTYELLOW_EX, power1, Fore.RESET, end=" ")
        print("\n")


class Lucky_numbers(Win_number):
    # this Lucky_numbers class program work for 5 random numbers and
    # power balls for Mega million lottery Lucky numbers
    def white_balls(self):  # five random numbers methoda/methode for Lucky_numbers
        print(Fore.LIGHTCYAN_EX, "Your lucky numbers:", Fore.RESET)
        list2 = []
        self.list2 = list2
        for num1 in range(5):
            r = random.randint(1, 20)
            list2.append(r)
        list2.sort()
        print(Fore.LIGHTMAGENTA_EX, *list2, Fore.RESET,  end=" ")

    def power_ball2(self):   # Power ball methoda/methode for Lucky numbers
        power2 = []
        for num2 in range(2):
            power2 = random.randint(1, 10)
        self.power2 = power2
        print(Fore.LIGHTYELLOW_EX, power2, Fore.RESET, end=" ")


class Grade(Lucky_numbers):  # Class doing calculate how much white ball and power ball you got and
                             # display how much you won/gain after the play

    def white_ballss(self):

        Win_number.white_balls(self)     # calling all methode in this class for making more usable in grading
        Win_number.power_ball1(self)     # and how much the winner got
        Lucky_numbers.white_balls(self)
        Lucky_numbers.power_ball2(self)
        print("\n")

        white_count = 0
        power_count = 0
        for elements in self.list1:
            if elements in self.list2:
                white_count = white_count + 1  # counting only the same random white ball in two lists

        if self.power1 == self.power2:  # count only when winner power ball and lucky power ball are equal:
            power_count += 1            # Because of, I don't have more than one list it'll display '1'
        if self.power1 != self.power2:  # when Power ball and lucky power ball aren't equal
            power_count += 0            # display zero

        print(Fore.LIGHTBLUE_EX, "You got", white_count, "White balls and", power_count, "power balls", Fore.RESET)

        if power_count == 1 and white_count == 5:
            print(Fore.LIGHTGREEN_EX, "Jackpot $324,000,000", Fore.RESET)  # highest value in the game
        elif power_count == 0 and white_count == 5:
            print(Fore.LIGHTGREEN_EX, "$1,000,000", Fore.RESET)
        elif power_count == 1 and white_count == 4:
            print(Fore.LIGHTGREEN_EX, "$10,000", Fore.RESET)
        elif power_count == 0 and white_count == 4:
            print(Fore.LIGHTGREEN_EX, "$100", Fore.RESET)
        elif power_count == 1 and white_count == 3:
            print(Fore.LIGHTGREEN_EX, "$100", Fore.RESET)
        elif power_count == 0 and white_count == 3:
            print(Fore.LIGHTGREEN_EX, "$7", Fore.RESET)
        elif power_count == 1 and white_count == 2:
            print(Fore.LIGHTGREEN_EX, "$7", Fore.RESET)
        elif power_count == 1 and white_count == 1:
            print(Fore.LIGHTGREEN_EX, "$4", Fore.RESET)
        elif power_count == 1 and white_count == 0:
            print(Fore.LIGHTGREEN_EX, "$4", Fore.RESET)
        else:
            print(Fore.RED, "Try Again", Fore.RESET)


obj1 = Grade()
obj1.white_ballss()

