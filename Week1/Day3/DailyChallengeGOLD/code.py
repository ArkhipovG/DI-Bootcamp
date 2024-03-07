choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()

if choice == 'encrypt':
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    print("Encrypted message:", encrypted_message)
elif choice == 'decrypt':
    message = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_message += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():
                decrypted_message += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_message += char
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")