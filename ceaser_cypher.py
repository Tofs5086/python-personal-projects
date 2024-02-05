# List of all lowercase alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'y',
            'z']


#  this is the function that will encrypt the user's input using the ceaser cipher technique
def encryption(plain_text, shift_key):
    cipher_text = ""

    # this loop will iterate through each character in the plain_text
    for char in plain_text:
        # this checks if the character is in the alphabet
        if char in alphabet:
            # this finds the index (position) of the character in the alphabet
            position = alphabet.index(char)

            # Shift the position by the specified shift_key
            new_position = (position + shift_key) % 26

            # Append the character at the new position to the cipher_text
            cipher_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, append it unchanged
            cipher_text += char

    # Print the encrypted text
    print(f"Here is the text after encryption: {cipher_text}")


#  this is the decryption function using Caesar Cipher
def decryption(cipher_text, shift_key):
    plain_text = ""

    # Iterate through each character in the cipher_text
    for char in cipher_text:
        # this checks if the character is in the alphabet
        if char in alphabet:
            # this will find the index (position) of the character in the alphabet
            position = alphabet.index(char)

            # this shifts the position back by the specified shift_key
            new_position = (position - shift_key) % 26

            # this appends the character at the new position to the plain_text
            plain_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, append it unchanged
            plain_text += char

    # Print the decrypted text
    print(f"Here is the text after decryption: {plain_text}")


# This is the main program loop
end_of_program = False
while not end_of_program:
    try:
        # User input: Encrypt or Decrypt
        what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n ").lower()

        # Raise an exception if the user doesn't type either 'encrypt' or 'decrypt'
        if what_to_do not in ['encrypt', 'decrypt']:
            raise ValueError("Please enter either 'encrypt' or 'decrypt'.")

        # User input: Text to encrypt or decrypt
        text = input('Type the word you want to encrypt:\n').lower()  # Convert to lowercase for consistency

        # User input: Shift key
        shift = int(input('Enter shift key: \n'))

        # Check if the shift key is within a valid range (0 to 25)
        if not (0 <= shift <= 25):
            raise ValueError("Shift key must be between 0 and 25 inclusive.")

        # Perform encryption or decryption based on user input
        if what_to_do == 'encrypt':
            encryption(plain_text=text, shift_key=shift)
        elif what_to_do == 'decrypt':
            decryption(cipher_text=text, shift_key=shift)

    except ValueError as e:
        print(f"Error: {e}")

    # Ask the user if they want to play again
    play_again = input("Type 'yes' to continue, type 'no' to exit. \n")

    # Check if the user wants to end the program
    if play_again.lower() == 'no':
        end_of_program = True
        print('Have a nice day! Goodbye.')
