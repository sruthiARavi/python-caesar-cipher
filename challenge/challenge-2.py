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
        if letter == " ":
            encrypted_text += letter
        else:
            original_index = alphabet.index(letter)
            shifted_index = (original_index + shift_amount) % 26
            encrypted_text += alphabet[shifted_index]
    print(f"Encrypted text: {encrypted_text}")

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter == " ":
            decrypted_text += letter
        else:
            shifted_index = alphabet.index(letter)
            decrypted_index = shifted_index - shift_amount
            if decrypted_index > 26:
                decrypted_index %= 26
            elif decrypted_index < 0:
                decrypted_index += 26
            decrypted_text += alphabet[decrypted_index]
    print(f"Decrypted text: {decrypted_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
