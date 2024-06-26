# print('type "help" for a list of commands')
# user_input = input('')
# while user_input != 'quit':
#   if user_input.lower() == 'help':
#     print('start - to start the car')
#     print('stop - to stop the car')
#     print('quit - to exit')
#   else: 
#     print("I don't understand that command")


command = ""
started = False
print('type "help" for a list of commands')
while True:
  command = input("> ").lower()
  if command == 'start':
    if started:
      print('Car is already running')
    else:
      started = True
      print('Car started...')
  elif command == 'stop':
    if not started:
      print('Car is already stopped')
    else:
      started = False
      print('Car stopped')
  elif command == 'help':
    print("""
start - to start the car
stop - to stop the car
quit - to exit
      """)
  elif command == 'quit':
    print("Don't forget to lock your car!")
    break
  else:
    print('Sorry, I do not understand that!')