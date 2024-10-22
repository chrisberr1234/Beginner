#Ask user for name
name = input("What is your name?: ")
print(name)

#Ask user for age
age = input("How old are you: ")
print(age)

#Ask user for city
city = input("What City do you currently live in: ")
print(city)

#Ask user what they enjoy
enjoy = input("What do you enjoy to do the most: ")
print(enjoy)

#Create output text
string = "Your name is {} and you are {} years old. You line in {} and you love {}"
output = string.format(name, age, city, enjoy)

#Print output to screen 
print(output)
