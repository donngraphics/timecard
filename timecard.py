
'''Getting warmed up'''


def time_card():
    '''Will eventually convert time to hours and minutes'''
    hour = input('Please input your hours: ')
    dec = input('Please input your decimal hours (after the decimal): ')

    if hour.isdigit() and dec.isdigit():

        convert = float(dec) * 60
        c_round = str(round((convert/100), 0))
        c_round2 = c_round[0:2].replace('.', '')
        print(
            f'Your hours stand at {hour} hours and {c_round2} minutes. Here\'s to you making time!')
    else:
        print("That isn't a number, try again...")


time_card()
print(time_card.__doc__)
