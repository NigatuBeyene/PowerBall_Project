
import random
from colorama import Fore


class Win_number():
# This Win_ number class program work for 5 random numbers and
# power balls for mega million lottery Winner numbers

    def white_balls(self):             # five random numbers methoda for Win_numbers
        print(Fore.LIGHTCYAN_EX, "Today's Powerball Winning Numbers:", Fore.RESET)
        list1 = []                     # Empity list use for put random numbers
        self.list1 = list1
        for num1 in range(5):          # select only five numbers in 20 numbers
            r = random.randint(1, 20)  # random numbers limit values
            list1.append(r)            # append random number in to 'list1'
        list1.sort()                   # makes ascending order for all  'list1'
        print(Fore.LIGHTMAGENTA_EX, *list1, Fore.RESET,  end=" ")

    def power_ball1(self):  # Power ball methoda for Winner numbers

        power1 = []
        for num1 in range(1):
            power1 = random.randint(1, 10)  # c
        self.power1 = power1
        print(Fore.LIGHTYELLOW_EX, power1, Fore.RESET, end=" ")
        print("\n")


class Lucky_numbers(Win_number):
    # this Lucky_numbers class program work for 5 random numbers and
    # power balls for mega million lottery Lucky numbers
    def white_balls(self):  # five random numbers methoda for Lucky_numbers
        print(Fore.LIGHTCYAN_EX, "Your lucky numbers:", Fore.RESET)
        list2 = []
        self.list2 = list2
        for num1 in range(5):
            r = random.randint(1, 20)
            list2.append(r)
        list2.sort()
        print(Fore.LIGHTMAGENTA_EX, *list2, Fore.RESET,  end=" ")

    def power_ball2(self):   # Power ball methoda for Lucky numbers
        power2 = []
        for num2 in range(2):
            power2 = random.randint(1, 10)
        self.power2 = power2
        print(Fore.LIGHTYELLOW_EX, power2, Fore.RESET, end=" ")

