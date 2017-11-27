def convert_numbers(str):       # Converts from type string to integer with error check.
    try:
        return int(str)
    except ValueError:
        return None

print('\n*** FACTORIAL OF A NUMBER ***')

end = 0
while (end != ('x')):                                           # End the program
    NumberInt = None
    factorial = 1

    # Input with error check.
    while (NumberInt == None or NumberInt < 1):
        NumberStr = input('\nWhat number du you want the factorial off? ')
        NumberInt = convert_numbers(NumberStr)

    # Finding the factorial.
    while NumberInt > 1:
        factorial = factorial * NumberInt
        NumberInt = NumberInt - 1

    print('The facturial of ', NumberStr, ' is ',factorial)

    end = input('\nNew calculation? Press \'ENTER\'.       End? Press \'x\'')

print('\n*** BYE ***')