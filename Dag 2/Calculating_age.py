def convert_numbers(str):       # Converts from type string to integer with error check.
    try:
        return int(str)
    except ValueError:
        return None

end = 0
while (end != ('x')):                                           # End the program
    print('\n***   CALCULATING YOUR AGE   ***\n')
    BirthYearInt = None
    NewerYearInt = None

    # Input first year with error check
    while (BirthYearInt == None or BirthYearInt < 1900 or BirthYearInt > 2100):
        BirtYearStr = input('The year you were born? ')
        BirthYearInt = convert_numbers(BirtYearStr)

    # Input second year with error check
    while (NewerYearInt == None or NewerYearInt < BirthYearInt or (NewerYearInt - BirthYearInt > 150)):
        NewerYearStr = input('For which year would you calculate your age? ')
        NewerYearInt = convert_numbers(NewerYearStr)

    AgeInt = (NewerYearInt - BirthYearInt)                      # Your age
    print('Your are', AgeInt, 'years old.')

    if (AgeInt == 100):                                         # 100 years
        print('Congratulation you are 100 years old!!')

    if (AgeInt == 1):                                           # One year
        print('Congratulation you are now 1 year!!')

    if (AgeInt >= 13 and AgeInt <= 19):                         # Teenager
        print('Hello teenager!!')

    AgeStr = str(AgeInt)

    if (int(AgeStr[-1]) == 0):                                  # New decade
        print('Welcome to a new decade!!!')

    BirthYearList = []
    digit = 0

    while (digit < 4):                                         # Sum of the digits
        BirthYearList.append(int(BirtYearStr[digit]))
        digit = digit + 1
    print('The sum of the digits of the birth year: ', sum(BirthYearList[:]))

    end = input('\nNew calculation? Press \'ENTER\'.       End? Press \'x\'')

print('\n*** BYE ***')