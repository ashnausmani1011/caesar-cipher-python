def caesar(text, shift, encrypt=True):

    # Check if shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Check if shift is between 1 and 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Reverse the shift for decryption
    if not encrypt:
        shift = -shift

    # Create the original alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create the shifted alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a translation table
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text
    return text.translate(translation_table)


# Function for encryption
def encrypt(text, shift):
    return caesar(text, shift)


# Function for decryption
def decrypt(text, shift):
    return caesar(text, shift, False)


# Test the decrypt function
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
