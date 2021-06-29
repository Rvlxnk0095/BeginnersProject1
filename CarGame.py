command = ''
while True:
    command = input('> ')
    if command == 'start':
        print("Car started...Ready to go!")
    elif command == 'stop':
        print("Car stopped!!!")
    elif command == 'help':
        print('''start: to start the car 
stop: to stop the car
quit: to exit''')
    elif command == 'quit':
        break
    else:
        print("We don't understand.")