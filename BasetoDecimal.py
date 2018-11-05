print("Base to Decimal Converter (Up to Base 36!)")
print("By Matthew Le Huenen")
print("----------------------------")

while True:

    print("")
    Input = input("Enter what you want converted: ")
    baseInput = input("Enter a Base: ")

    if Input.isalnum() and baseInput.isdigit():

        Input = Input.lower()
        inputList = list(Input)
        base = int(baseInput)
        exponent = (len(Input) - 1)
        number = 0

        if (base == 0) or (base == 1) or (base > 36):
            print("")
            print("Invalid Base")
            print("")

        else:
            for x in range(0, len(Input)):
                listElement = inputList.pop(0)

                if listElement.isalpha():
                    listElement = ord(listElement) - 87

                if (int(listElement) >= base):
                    number = "Invalid Character"
                    break

                numberAddition = int(listElement)*(base**exponent)
                exponent = exponent - 1
                number = number + numberAddition

            print("")
            print(number)
            print("")

    else:
        print("")
        print("Invalid Input")
        print("")

    try_again = (input("Press 0 to exit, or anything else to run the program again. "))
    if try_again.isdigit():
        if int(try_again) == 0:
            break