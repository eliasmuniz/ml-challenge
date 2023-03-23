sentence = "Hello world" 
nrOfCharacters = len(sentence)
print("The sentence 'Hello World' has {} characters".format(nrOfCharacters))
print(f"The sentence 'Hello World' has {nrOfCharacters} characters")
print(sentence.count('o'))
print(sentence.find('e'))
sometext = "Hey you, how are you doing?"
print(sometext.rfind("you"))
#  rfind returns the lasts occurrence of a string. So in sometext 
#  we have the word "you" twice. rfind returns 17 meaning that
#  the last time that it found "you" is starting at position 
#  17 (counting from 0).

# Changes the string to upper case
print(sometext.upper())

# Splits the string on a character and returns it as list items. You'll learn about lists later
print(sometext.split(","))
print(sometext.split(" "))

# Replaces strings
print(sometext.replace("?","!"))