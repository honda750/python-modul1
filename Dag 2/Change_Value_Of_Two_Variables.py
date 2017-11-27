
print('\n*** CHANGE THE VALUES OF TWO VARIABLES ***\n')

VariableOne = input('Write the value of the first variable: ')
VariableTwo = input('Write the value of the second variable: ')

print('Variable one = ',VariableOne)
print('Variable two = ',VariableTwo)

# Change the values of the variables
VariableOne, VariableTwo = VariableTwo, VariableOne

print('Variable one are now = ',VariableOne)
print('Variable two are now = ',VariableTwo)
