print("Decimal to Base Converter (WIP)")
print("By Matthew Le Huenen")
print("----------------------------")

while True: 

    print("")
    numberInput = input("Enter a number: ")
    baseInput = input("Enter a base: ")

    if numberInput.isdigit() and baseInput.isdigit():

        number = int(numberInput)
        base = int(baseInput)
        convertedNumber = ""

        if (base == 0) or (base == 1):
            print("")
            print("Invalid Base")
            print("")

        elif (number == 0):
            print("")
            print("0")
            print("")

        else:

            while (number > 0):
                remainder = number % base
                convertedNumber = convertedNumber + str(remainder)
                number = number // base

                if (number < base):
                    convertedNumber = convertedNumber + str(number)
                    print("")
                    print(convertedNumber[::-1])
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
