# stores a words in a list then checks the length for each word then prints words wiht an odd word length.
words = []

num = int(input("How many words do you want?: "))

for word in range(0, num):
	word = input("Enter your words: ")

	words.append(word)

odd_words = [w for w in words if len(w) % 2 != 0]  # Use list comprehension to filter odd words

if odd_words:
    print("The words are: ", ", ".join(odd_words))  # Print odd words with comma separation
else:
    print("There are no odd words")
