import time
import os
while True:
    words = """Terminal Calculator
    [1]: Math Operators
    [2]: Odd or Even
    [3]: Temperature Checker
    [4]: Exit"""
    for i in words:
        print(i, end="", flush= True)
        time.sleep(0.01)
    print()
    def cal():
        os.system("clear")
        ope = input("operators: + - / x --> ")
        print("press empty enter to totalize...")
        total = None
        while True:
            num = input("num: ")
            if num == "":
                print("total: ", total)
                break
            num = float(num)
            if total is None:
                total = num
            else:
                if ope == "+":
                    total += num
                elif ope == "-":
                    total -= num
                elif ope "x":
                    total *= num
                elif ope == "/":
                    total /= num
            print("total:", total)
    def oddeven():
        os.system("clear")
        number = int(input("numbers to check: "))
        if number % 2 == 0:
            print("It's Even")
        elif number % 2 != 0:
            print("It's Odd")
        else:
            print("invalid input!")
    def temp():
        os.system("clear")
        temperature = float(input("Enter the temperature: "))
        if temperature <= 20:
            print("it's cold!")
        elif temperature <= 30:
            print("it's a bit cold..")
        else:
            print("it's hot..")
    x = int(input("Choose the tool you want to use: "))
    if x == 1:
        cal()
    elif x == 2:
        oddeven()
    elif x == 3:
        temp()
    elif x == 4:
        print("thanks, bye!")
        break
    else:
        print("what do you mean?")
