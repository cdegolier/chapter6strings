#Exercise 3:
#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def countLetters(str, ch):
	fruit = str
	count = 0
	for char in fruit:
		if char == ch:
			count = count + 1
	print (count)

countLetters("hi how are you?" , "h")
