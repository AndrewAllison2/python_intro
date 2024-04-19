# greeting = 'Hello World!'
# print(greeting)

# name="John Smith"
# age=20
# is_new_patient=True

# print(name, age, is_new_patient)

# First: 10.1
# Second: 20
# Sum: 30.1

# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " + sum)

# NOTE Python doesnt know how to concatinate a float with a string


# temp = 5

# if temp > 30:
#   print("It's a hot day!")
# elif temp > 20:
#   print("It's pretty nice out!")
# elif temp < 15:
#   print("Don't go outside!")

# weight = input("Weight: ")
# measure = input("(K)g or (L)bls: ")
# if measure.lower() == "k":
#   print("Weight: " + weight + " " + "Kg")
# elif measure.lower() == "l":
#   print("Weight: " + weight + " " + "Lbs")
# elif measure.lower() != "l" or measure.lower() != "k":
#   print("Please select a weight measurement!")


weight = int(input("Weight: "))
unit = input("(K)g or (L)bls: ")
if unit.upper() == "K":
  converted = weight / 0.45
  print("weight in Lbs: " + str(converted))
else:
  converted = weight * 0.45
  print("Weight in Kgs: " + str(converted))


