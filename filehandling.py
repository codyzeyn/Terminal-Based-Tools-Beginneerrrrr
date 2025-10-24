import time
def create():
    filename = input("name of a file: ")
    print("")
    print("now type something inside the file. press empty enter to stop. ")
    with open(filename, "w") as file:
        while True:
            text = input("type to a file; ")
            file.write("\n" + text)
            if text == "":
                print("file now is created")
                break
def reading():
    name = input("name of the file? --> ")
    with open(name, "r") as file:
        txt = file.read()
        print()
        print(txt)
def add():
    name = input("file name you want to add lines --> ")
    print("add something to a file. press empty nothing to stop")
    with open(name, "a") as file:
        while True:
            intext = input("type something that will adds to a file: ")
            file.write("\n" + intext)
            if intext == "":
                break
    
print("First terminal based tool (text editor)")
a = input("do you want to open the tool? yes/no --> ").lower()
if a == "yes":
    ani = """[1]: File editor/creator
[2]: File reader
[3]: File appender
[4]: exit,.,"""
for i in ani:
    print(i, end="", flush= True)
    time.sleep(0.02)
print()
while True:
    b = int(input("Choose the number/tool you want to use; "))
    if b == 1:
        create()
    elif b == 2:
        reading()
    elif b == 3:
        add()
    elif b == 4:
        break
    else:
        print("what do you mean?")
