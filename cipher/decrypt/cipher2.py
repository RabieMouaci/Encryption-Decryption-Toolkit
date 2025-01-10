def decrypt_cipher():
    #Decrypt Level 1
    def level_one_decrypt():
        alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
        shift = int(input("Enter the module of shifting used for encryption: ")) % 26
        message = input("Enter the encrypted message: ")
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                new_index = (alphabet.index(char) - shift) % 26
                new_char = alphabet[new_index]
                decrypted_message += new_char.upper() if is_upper else new_char
            else:
                decrypted_message += char
        print("Decrypted message:", decrypted_message)

    #Decrypt Level 2
    def level_two_decrypt():
        alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
        key = input("Enter the keyword used for encryption: ").lower()
        message = input("Enter the encrypted message: ")
        extended_key = ""
        key_index = 0
        for char in message:
            if char.isalpha():
                extended_key += key[key_index % len(key)]
                key_index += 1
            else:
                extended_key += char
        decrypted_message = ""
        for i, char in enumerate(message):
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                shift = alphabet.index(extended_key[i])
                new_index = (alphabet.index(char) - shift) % 26
                new_char = alphabet[new_index]
                decrypted_message += new_char.upper() if is_upper else new_char
            else:
                decrypted_message += char
        print("Decrypted message:", decrypted_message)

    #Decrypt Level 3
    def level_three_decrypt():
        # Reverse Columnar Transposition
        def columnar_transposition_decrypt(ciphertext, key):
            key_order = sorted((int(k), i) for i, k in enumerate(key))
            num_columns = len(key)
            num_rows = len(ciphertext) // num_columns
            extra_chars = len(ciphertext) % num_columns
            column_lengths = [num_rows + (1 if i < extra_chars else 0) for _, i in key_order]
            columns = []
            start = 0
            for length in column_lengths:
                columns.append(ciphertext[start:start + length])
                start += length
            original_order = sorted((i, col_index) for col_index, (_, i) in enumerate(key_order))
            result = ""
            for row in range(num_rows + (1 if extra_chars > 0 else 0)):
                for _, col_index in original_order:
                    if row < len(columns[col_index]):
                        result += columns[col_index][row]
            return result

        # Reverse Vigenère Cipher
        def vigenere_decrypt(message, key):
            alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
            extended_key = ""
            key_index = 0
            for char in message:
                if char.isalpha():
                    extended_key += key[key_index % len(key)].lower()
                    key_index += 1
                else:
                    extended_key += char
            decrypted_message = ""
            for i, char in enumerate(message):
                if char.isalpha():
                    is_upper = char.isupper()
                    char = char.lower()
                    shift = alphabet.index(extended_key[i])
                    new_index = (alphabet.index(char) - shift) % 26
                    new_char = alphabet[new_index]
                    decrypted_message += new_char.upper() if is_upper else new_char
                else:
                    decrypted_message += char
            return decrypted_message

        key_vigenere = input("Enter the keyword used for the Vigenère cipher: ")
        key_columnar = input("Enter the numeric key used for columnar transposition (e.g., 3142): ")
        encrypted_message = input("Enter the encrypted message: ")

        #Reverse Columnar Transposition
        intermediate_message = columnar_transposition_decrypt(encrypted_message, key_columnar)

        # Reverse Vigenère Cipher
        final_message = vigenere_decrypt(intermediate_message, key_vigenere)

        print("Decrypted message:", final_message)

    # Main menu
    print("Select a level to decrypt:")
    print("1. Level 1: Basic Shift Cipher")
    print("2. Level 2: Vigenère Cipher")
    print("3. Level 3: Hybrid Cipher (Vigenère + Columnar Transposition)")

    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        level_one_decrypt()
    elif level == "2":
        level_two_decrypt()
    elif level == "3":
        level_three_decrypt()
    else:
        print("Invalid choice. Please restart the program and select a valid level.")


decrypt_cipher()
