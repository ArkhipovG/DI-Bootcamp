reverseinp = input("Enter a sentence: ")

words = reverseinp.split()

reversed_sentence = ' '.join(words[::-1])

print("Reversed sentence:", reversed_sentence)