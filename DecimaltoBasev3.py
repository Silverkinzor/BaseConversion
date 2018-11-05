print("Decimal to Base Converter (Up to Base 36!)")
print("By Matthew Le Huenen")
print("----------------------------")

while True: 

    print("")
    numberInput = input("Enter a number: ")
    baseInput = input("Enter a base: ")
    baseList = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    if numberInput.isdigit() and baseInput.isdigit():

        number = int(numberInput)
        base = int(baseInput)
        convertedNumber = ""

        if (base == 0) or (base == 1) or (base > 36):
            print("")
            print("Invalid Base")
            print("")

        else:

            while True:
                remainder = number % base

                if (number < base):

                    if (remainder < 10):
                        convertedNumber = convertedNumber + str(number)

                    else:
                        remainderChar = baseList[remainder - 10]
                        convertedNumber = convertedNumber + str(remainderChar)

                    break

                elif (remainder > 9):
                    remainderChar = baseList[remainder - 10]
                    convertedNumber = convertedNumber + str(remainderChar)

                else:
                    convertedNumber = convertedNumber + str(remainder)

                number = number // base

            print("")
            print(convertedNumber[::-1])
            print("")

    else:
        print("")
        print("Invalid Input")
        print("")

    try_again = (input("Press 0 to exit, or anything else to run the program again. "))
    if try_again.isdigit():
        if int(try_again) == 0:
            break
