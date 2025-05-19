Secret_number = 6
gauss_count = 0
gauss_limit = 3

while gauss_count < gauss_limit:
    gauss = int(input('Enter a number between 1 to 10: '))
    gauss_count += 1
    if gauss == Secret_number:
        print('Hurray, You\'ve won the game! ')
        break
else:
    print('Sorry, You\'ve loss the game. Plz Try again.. ')
