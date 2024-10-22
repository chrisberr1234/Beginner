for number in range(1,1001):
    print(number)

s_vowels = "aeiou"
vowels = 0
consonants = 0

your_name = input("Please Input Your Name: ")

for letter in your_name:
    if letter.lower() in s_vowels:
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print('Your name has {}'.format(vowels), 'vowels and {} consonants'.format(consonants))
