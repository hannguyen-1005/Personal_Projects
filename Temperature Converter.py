# Name: Han Gia Nguyen
# UID: U33382209
# Description: The program shows the options and takes the input as the selection of option (with validation). 
# It then asks for the temperature to convert and converts according to the selection.
# The program prints the result from the dictionary and then asks for continuing. The main function will continuously be called unless a 'no' is entered.
def options():
    print('This program will convert tempearatures for you!\n1. Convert from Celsius to Fahrenheit\n2. Convert from Celsius to Kelvin\n3. Convert from Fahrenheit to Celsius\n4.Convert from Fahrenheit to Kelvin\n5. Convert from Kelvin to Celsius\n6. Convert from Kelvin to Fahrenheit ')
def cf(t):
    return (9/5)*t + 32
def ck(t):
    return t+273.15
def fc(t):
    return (5/9)*(t-32)
def fk(t):
    return (5/9)*(t-32) + 273.15
def kc(t):
    return t - 273.15
def kf(t):
    return (9/5)*(t - 273.15) + 32
def main():
    options()
    opt = int(input('Please select an option: '))
    while (opt < 1) or (opt > 6):
        opt = int(input('Invalid choice. Please re-select an option: '))
    temp = float(input('Enter a temperature: '))
    convert = {'1':f'{temp} degrees Celsius is {cf(temp):.2f} degrees Fahrenheit',
               '2':f'{temp} degrees Celsius is {ck(temp):.2f} degrees Kelvin',
               '3':f'{temp} degrees Fahrenheit is {fc(temp):.2f} degrees Celsius',
               '4':f'{temp} degrees Fahrenheit is {fk(temp):.2f} degrees Kelvin',
               '5':f'{temp} degrees Kelvin is {kc(temp):.2f} degrees Celsius',
               '6':f'{temp} degrees Kelvin is {kf(temp):.2f} degrees Fahrenheit'}
    print (convert.get(str(opt),0))
    while r:=input('Would you like to convert another temperature? ').lower() != 'no':
        main()
    else:
        print('',end='')
main()