"""
    Vær      Celsius Farenheit
"""
def convert_numbers(str):       # Converts from type string to integer with error check.
    try:
        return int(str)
    except ValueError:
        return None


farenheit = None
celsius = None

temp= input('Do you want Celsius C or Farenheit F ? : ')

if (temp == 'C'):
    celsius = ((farenheit - 32) / 9) * 5
elif (temp == 'F'):

farenheit = 32

celsius = ((farenheit -32)/9)*5

print (celsius)


farenheit =  ((9 * celsius + 160)/5)