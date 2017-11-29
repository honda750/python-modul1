def celsiusToFarenheit():
    myInput = int(input('Enter a temperatre in Celsius: '))
    tempInFarenheit = (myInput * 9 +160) / 5
    print('The temp of', myInput, 'in celsius is', tempInFarenheit, (' in fahrenheit'))


def farenheitToCelsius():
    myInput = int(input('Enter a temperatre in Farenheit: '))
    tempInCelsius = ((myInput - 32) / 9) * 5
    print('The temp of', myInput, 'in farenheit is', tempInCelsius, (' in Celsius'))

answer = None
while (answer != 'c') or (answer != 'f'):
    optionSelected = input('Enter - c - for output in celsius and enter - f - for Farenheit: ')
    if(optionSelected == 'c'):
        celsiusToFarenheit()
    elif(optionSelected == 'f'):
        farenheitToCelsius()
    print(answer)


