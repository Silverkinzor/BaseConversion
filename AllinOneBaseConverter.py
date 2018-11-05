print("All in One Base Converter (Up to Base 36!)")
print("By Matthew Le Huenen")
print("----------------------------")
try_again = ''


# Todo: Direct base to base conversion

while try_again != '0':

    print("")
    print("1. Decimal to Base")
    print("2. Base to Decimal")
    print("0. Exit")

    try_again = input()
    try_again.strip()
    if try_again.isdigit():

        if try_again == '1': # Decimal to Base

            print("") # inputs and setup
            numberInput = input("Enter a number: ")
            baseInput = input("Enter a base: ")
            baseList = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

            if numberInput.isdigit() and baseInput.isdigit(): # input check

                number = int(numberInput) # setup
                base = int(baseInput)
                convertedNumber = ""

                if (base == 0) or (base == 1) or (base > 36): # input check
                    print("")
                    print("Invalid Base")

                else:

                    while True: # loops until number is converted
                        remainder = number % base # Obtain remainder

                        if (number < base): # handle remainder in the case of number < base, runs once

                            if (remainder < 10):
                                convertedNumber = convertedNumber + str(number)

                            else:
                                remainderChar = baseList[remainder - 10]
                                convertedNumber = convertedNumber + str(remainderChar)

                            break

                        elif (remainder > 9): # handle remainder in the case of number > base
                            remainderChar = baseList[remainder - 10]
                            convertedNumber = convertedNumber + str(remainderChar)

                        else: # handle remainder in the case of number > base, but remainder < 10
                            convertedNumber = convertedNumber + str(remainder)

                        number = number // base # Remainder handled, move on to the next, repeat the while loop

                    print("")
                    print(convertedNumber[::-1]) # print backwards for proper answer, this is the method learned in comp sci class

            else:
                print("")
                print("Invalid Input")

        elif try_again == '2':
            
            print("")
            Input = input("Enter what you want converted: ")
            baseInput = input("Enter a Base: ")

            if Input.isalnum() and baseInput.isdigit(): # input validation

                Input = Input.lower() # setup
                inputList = list(Input) # store each input character into a list
                base = int(baseInput)
                exponent = (len(Input) - 1)
                number = 0

                if (base == 0) or (base == 1) or (base > 36):
                    print("")
                    print("Invalid Base")

                else:
                    for x in range(0, len(Input)): # for each element in the list
                        listElement = inputList.pop(0) # take the element in the front of the list

                        if listElement.isalpha(): # alphabet to number
                            listElement = ord(listElement) - 87

                        if (int(listElement) >= base): # input validation
                            number = "Invalid Character"
                            break

                        numberAddition = int(listElement)*(base**exponent) # multiply it by base multiplied by exponent
                        exponent = exponent - 1 # reduce exponent
                        number = number + numberAddition # add it to the total answer

                    print("") # all that has the effect of converting base to decimal, eg. 120 in base 3 to 10, (1*3^2)+(2*3^1)+(0*3^0) = 15
                    print(number) # print answer

            else:
                print("")
                print("Invalid Input")