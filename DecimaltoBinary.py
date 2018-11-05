print("Decimal to Binary Converter")
print("By Matthew Le Huenen")
print("----------------------------")

while True: 

    print("")
    x = input ("Enter a number: ")

    if x.isdigit():

        y = int(x)
        g = ""

        if (y == 0):
            print("")
            print("0")
            print("")
        else:

            while (y > 0):
                z = y % 2
                g = g + str(z)
                y = y // 2

                if (y == 1):
                    g = g + str(1)
                    print("")
                    print(g[::-1])
                    print("")
                    break

    else:
        print("")
        print("Invalid Input")
        print("")

    try_again = (input("Press 0 to exit, or anything else to run the program again. "))
    if try_again.isdigit():
        if int(try_again) == 0:
            break