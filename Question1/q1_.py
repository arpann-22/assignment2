def shift_inside_range(ch, start, end, shift):

    range_size = ord(end) - ord(start) + 1
    return chr((ord(ch) - ord(start) + shift) % range_size + ord(start))


def encrypt_file(shift1, shift2):
    # Reading the original text
    with open("raw_text.txt", "r") as file:
        original_text = file.read()

    encrypted_text = ""

    # Encrypting character by character
    for ch in original_text:

        # Lowercase a-m → shift forward by shift1 * shift2
        if 'a' <= ch <= 'm':
            encrypted_text += shift_inside_range(ch, 'a', 'm', shift1 * shift2)

        # Lowercase n-z → shift backward by shift1 + shift2
        elif 'n' <= ch <= 'z':
            encrypted_text += shift_inside_range(ch, 'n', 'z', -(shift1 + shift2))

        # Uppercase A-M → shift backward by shift1
        elif 'A' <= ch <= 'M':
            encrypted_text += shift_inside_range(ch, 'A', 'M', -shift1)

        # Uppercase N-Z → shift forward by shift2 squared
        elif 'N' <= ch <= 'Z':
            encrypted_text += shift_inside_range(ch, 'N', 'Z', shift2 ** 2)

        else:
            encrypted_text += ch

    # Save encrypted text
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("Encrypted file created → encrypted_text.txt")


def decrypt_file(shift1, shift2):
    # Read the encrypted text
    with open("encrypted_text.txt", "r") as file:
        encrypted_text = file.read()

    decrypted_text = ""

    # Reverse the encryption
    for ch in encrypted_text:

        # Reverse lowercase a-m rule
        if 'a' <= ch <= 'm':
            decrypted_text += shift_inside_range(ch, 'a', 'm', -(shift1 * shift2))

        # Reverse lowercase n-z rule
        elif 'n' <= ch <= 'z':
            decrypted_text += shift_inside_range(ch, 'n', 'z', (shift1 + shift2))

        # Reverse uppercase A-M rule
        elif 'A' <= ch <= 'M':
            decrypted_text += shift_inside_range(ch, 'A', 'M', shift1)

        # Reverse uppercase N-Z rule
        elif 'N' <= ch <= 'Z':
            decrypted_text += shift_inside_range(ch, 'N', 'Z', -(shift2 ** 2))

       
        else:
            decrypted_text += ch

    # Save decrypted text
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

    print("Decrypted file created → decrypted_text.txt")


def verify_decryption():
    # Read original file
    with open("raw_text.txt", "r") as file:
        original_text = file.read()

    # Read decrypted file
    with open("decrypted_text.txt", "r") as file:
        decrypted_text = file.read()

    # Compare both texts
    if original_text == decrypted_text:
        print("SUCCESS → Decryption matches original ✔✔✔")
    else:
        print("FAILED → Decryption does NOT match original ✗✗✗")


def main():
    print("Encryption + Decryption tester")
    print("Make sure raw_text.txt exists in this folder!\n")

    print("=== ENCRYPTING FILE ===")
    shift1 = int(input("Enter shift1 number: "))
    shift2 = int(input("Enter shift2 number: "))

    encrypt_file(shift1, shift2)

    print("\n=== DECRYPTING FILE ===")
    print("Using the same shift values...")
    decrypt_file(shift1, shift2)

    print("\n=== VERIFYING DECRYPTION ===")
    verify_decryption()

    print("\nProgram finished.")


# Start the program
main()
