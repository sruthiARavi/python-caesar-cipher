import string

# initializing empty list
alphabet = []
# using string for filling alphabets
alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Separate encryption function
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter == " ":
            encrypted_text += letter
        else:
            original_index = alphabet.index(letter)
            shifted_index = (original_index + shift_amount) % len(alphabet)
            encrypted_text += alphabet[shifted_index]
    print(f"Encrypted text: {encrypted_text}")

#Separate decryption function
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter == " ":
            decrypted_text += letter
        else:
            shifted_index = alphabet.index(letter)
            decrypted_index = (shifted_index - shift_amount) % len(alphabet)
            if decrypted_index < 0:
                decrypted_index += len(alphabet)
            decrypted_text += alphabet[decrypted_index]
    print(f"Decrypted text: {decrypted_text}")

def caesar(encode_or_decode, text, shift):
    output_text = ""
    output_index = -1

    # encode -> add shift, decode -> subtract shift
    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        if letter == " ":
            output_text += letter

        else:
            current_index = alphabet.index(letter)
            output_index = (current_index + shift) % len(alphabet)
            if output_index < 0:
                output_index += len(alphabet)
            output_text += alphabet[output_index]

    print(f"Here is the {encode_or_decode}d result : {output_text}")

caesar(direction, text, shift)
