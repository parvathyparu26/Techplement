import string
import random



f1 = list(string.ascii_lowercase)
f2 = list(string.ascii_uppercase)
f3 = list(string.digits)
f4 = list(string.punctuation)


user_input = input("How many characters do you want in your password? ")



while True:

	

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break


		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")



random.shuffle(f1)
random.shuffle(f2)
random.shuffle(f3)
random.shuffle(f4)



part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))



result = []

for x in range(part1):

	result.append(f1[x])
	result.append(f2[x])

for x in range(part2):

	result.append(f3[x])
	result.append(f4[x])



random.shuffle(result)



password = "".join(result)
print("Strong Password: ", password)
