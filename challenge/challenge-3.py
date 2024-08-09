import string
from art import logo
# initializing empty list
alphabet = []
# using string for filling alphabets
alphabet = list(string.ascii_lowercase)

def caesar(encode_or_decode, text, shift):
    output_text = ""
    output_index = -1

    # encode -> add shift, decode -> subtract shift
    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            output_text += letter

        else:
            current_index = alphabet.index(letter)
            output_index = (current_index + shift) % len(alphabet)
            if output_index < 0:
                output_index += len(alphabet)
            output_text += alphabet[output_index]

    print(f"Here is the {encode_or_decode}d result : {output_text}")

print(logo)
go_again = "yes"
while go_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
print("Goodbye!")
