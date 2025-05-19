command = ''
started = False

while True:
    command = input('What do you want?: > ').lower()
    if command == 'start':
        if started:
            print('Car is already Started')
        else:
            started = True
            print('Car is Starting')
    elif command == 'stop':
        if not started:
            print('car is already Stoped')
        else:
            started = False
            print('car is Stoping')
    elif command == 'help':
        print(""" 
Type: 
Start - to Start the game
stop - to stop the game
quit - to Quit the game
 """)
    elif command == 'quit':
        break
    else:
        print('I don\'t understand what are you saying. please type help to know menu')
