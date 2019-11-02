me = 1

while me != 2:
    print("beginning function")
    print("Press m to open a nested menu")
    pinput = input()
    if pinput == "m":
        while pinput != "exit":
            print("type exit to exit")
            pinput = input()