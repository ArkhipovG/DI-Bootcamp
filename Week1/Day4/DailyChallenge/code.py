matrix_str = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""

# Convert the matrix string into a 2D list
matrix = [list(row) for row in matrix_str.strip().split('\n')]
print(matrix)
# Transpose the matrix to make columns accessible easily
transposed_matrix = list(zip(*matrix))
print(transposed_matrix)
# Initialize the decrypted message
decoded_message = ''

# Loop through each column
for column in transposed_matrix:
    word = ''  # Initialize the word for the current column
    for char in column:
        if char.isalpha():
            word += char  # Append alphabetic characters to the current word
            print(word)
        elif word:  # If non-alphabetic character encountered and word is not empty
            decoded_message += word + ' '  # Add the word to the decoded message
            word = ''  # Reset the word
    if word:  # If word is not empty after processing the column
        decoded_message += word + ' '  # Add the word to the decoded message

    print(word)
# Print the decrypted message
print(decoded_message)
print(decoded_message.strip())