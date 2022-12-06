
from colorama import Fore

from powerBall_utility import Win_number
from powerBall_utility import Lucky_numbers


class Grade(Lucky_numbers):

    def white_ballss(self):

        Win_number.white_balls(self)
        Win_number.power_ball1(self)
        Lucky_numbers.white_balls(self)
        Lucky_numbers.power_ball2(self)
        print("\n")
        count1 = 0
        count = 0

        for elements1 in self.list1:
            if elements1 in self.list2:
                count1 = count1 + 1

        if self.power1 == self.power2:
            count += 1
        if self.power1 != self.power2:
            count += 0

        print(Fore.LIGHTBLUE_EX, "You got", count1, "White balls and", count, "power balls", Fore.RESET)

        if count == 1 and count1 == 5:
            print(Fore.LIGHTGREEN_EX, "Jackpot $324,000,000", Fore.RESET)
        elif count == 0 and count1 == 5:
            print(Fore.LIGHTGREEN_EX, "$1,000,000", Fore.RESET)
        elif count == 1 and count1 == 4:
            print(Fore.LIGHTGREEN_EX, "$10,000", Fore.RESET)
        elif count == 0 and count1 == 4:
            print(Fore.LIGHTGREEN_EX, "$100", Fore.RESET)
        elif count == 1 and count1 == 3:
            print(Fore.LIGHTGREEN_EX, "$100", Fore.RESET)
        elif count == 0 and count1 == 3:
            print(Fore.LIGHTGREEN_EX, "$7", Fore.RESET)
        elif count == 1 and count1 == 2:
            print(Fore.LIGHTGREEN_EX, "$7", Fore.RESET)
        elif count == 1 and count1 == 1:
            print(Fore.LIGHTGREEN_EX, "$4", Fore.RESET)
        elif count == 1 and count1 == 0:
            print(Fore.LIGHTGREEN_EX, "$4", Fore.RESET)

        else:
            print(Fore.RED, "Try Again", Fore.RESET)

