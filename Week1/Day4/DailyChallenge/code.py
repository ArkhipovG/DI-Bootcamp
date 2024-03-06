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

matrix = [list(row) for row in matrix_str.strip().split('\n')]

transposed_matrix = list(zip(*matrix))

decoded_message = ''

for column in transposed_matrix:
    word = ''
    for char in column:
        if char.isalpha():
            word += char
        elif word:
            decoded_message += word + ' '
            word = ''
    if word:
        decoded_message += word

print(f"Neo, {decoded_message.strip()}")
