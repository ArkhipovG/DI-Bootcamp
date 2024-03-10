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

encrypted_message = [''.join(i) for column in transposed_matrix for i in column if i.isalpha()]
for i in range(len(encrypted_message)):
    if encrypted_message[i] == 'i' and encrypted_message[i+1] == 's':
        encrypted_message.insert(i+2, ' ')
encrypted_message = "Neo, " + ''.join(encrypted_message)
print(encrypted_message)










# matrix_str = """
# 7ii
# Tsx
# h%?
# i #
# sM
# $a
# #t%
# ^r!
# """
#
# matrix = [list(row) for row in matrix_str.strip().split('\n')]
#
# transposed_matrix = list(zip(*matrix))
# print(transposed_matrix)
# decoded_message = ''
#
#
# for column in transposed_matrix:
#     word = ''
#     for char in column:
#         if char.isalpha():
#             word += char
#         elif word:
#             decoded_message += word + ' '
#             word = ''
#     if word:
#         decoded_message += word
#
# print(f"Neo, {decoded_message.strip()}")
