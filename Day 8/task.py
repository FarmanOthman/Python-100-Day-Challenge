print("Welcome to the Caesar Cipher")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

user_choice = input("Write 1 for encryption or 2 for decryption: ")
text = input("Enter your text: ").lower()
shift = int(input("Enter the shift number: "))

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            new_alphabet_index = (alphabet_index + shift) % len(alphabet)
            encrypted_text += alphabet[new_alphabet_index]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            new_alphabet_index = (alphabet_index - shift) % len(alphabet)
            decrypted_text += alphabet[new_alphabet_index]
        else:
            decrypted_text += letter
    return decrypted_text

def progress(user_choice):
    if user_choice == "1":
        return encrypt(text, shift)
    elif user_choice == "2":
        return decrypt(text, shift)
    else:
        return "Invalid choice"

result = progress(user_choice)
print(result)
