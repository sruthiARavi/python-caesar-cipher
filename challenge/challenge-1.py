import string

# initializing empty list
alphabet = []
# using string for filling alphabets
alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        original_index = alphabet.index(letter)
        shifted_index = (original_index + shift_amount) % 26
        encrypted_text += alphabet[shifted_index]
    print(f"Encrypted text: {encrypted_text}")

if direction == "encode":
    encrypt(text, shift)

