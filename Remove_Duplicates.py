string = input("Enter string: ")
word = ""

for char in string:
    if char not in word:
        result += word

print("Unique string:", word)
