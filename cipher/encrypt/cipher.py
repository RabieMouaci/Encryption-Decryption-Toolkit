def shift_cipher():
    def level_one():
        alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
        shift = int(input("Enter the module of shifting: ")) % 26
        message = input("Enter your message (max 1000 characters): ")
        ciphered_message = ""
        for char in message:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                new_index = (alphabet.index(char) + shift) % 26
                new_char = alphabet[new_index]
                ciphered_message += new_char.upper() if is_upper else new_char
            else:
                ciphered_message += char
        print("Ciphered message:", ciphered_message)

    def level_two():
        alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
        key = input("Enter the keyword for the Vigenère cipher: ").lower()
        message = input("Enter your message (max 1000 characters): ")
        extended_key = ""
        key_index = 0
        for char in message:
            if char.isalpha():
                extended_key += key[key_index % len(key)]
                key_index += 1
            else:
                extended_key += char
        ciphered_message = ""
        for i, char in enumerate(message):
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                shift = alphabet.index(extended_key[i])
                new_index = (alphabet.index(char) + shift) % 26
                new_char = alphabet[new_index]
                ciphered_message += new_char.upper() if is_upper else new_char
            else:
                ciphered_message += char
        print("Ciphered message:", ciphered_message)

    def level_three():
        def vigenere_encrypt(message, key):
            alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'
            extended_key = ""
            key_index = 0
            for char in message:
                if char.isalpha():
                    extended_key += key[key_index % len(key)].lower()
                    key_index += 1
                else:
                    extended_key += char
            ciphered = ""
            for i, char in enumerate(message):
                if char.isalpha():
                    is_upper = char.isupper()
                    char = char.lower()
                    shift = alphabet.index(extended_key[i])
                    new_index = (alphabet.index(char) + shift) % 26
                    new_char = alphabet[new_index]
                    ciphered += new_char.upper() if is_upper else new_char
                else:
                    ciphered += char
            return ciphered

        def columnar_transposition_encrypt(message, key):
            key_order = sorted((int(k), i) for i, k in enumerate(key))
            columns = [""] * len(key)
            for i, char in enumerate(message):
                columns[i % len(key)] += char
            transposed = ""
            for _, col_index in key_order:
                transposed += columns[col_index]
            return transposed

        key_vigenere = input("Enter the keyword for the Vigenère cipher: ")
        message = input("Enter your message (max 1000 characters): ")
        vigenere_result = vigenere_encrypt(message, key_vigenere)
        key_columnar = input("Enter the numeric key for columnar transposition (e.g., 3142): ")
        final_cipher = columnar_transposition_encrypt(vigenere_result, key_columnar)
        print("Encrypted message:", final_cipher)

    # Main menu
    print("Select a level:")
    print("1. Level 1: Basic Shift Cipher")
    print("2. Level 2: Vigenère Cipher")
    print("3. Level 3: Hybrid Cipher (Vigenère + Columnar Transposition)")

    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        level_one()
    elif level == "2":
        level_two()
    elif level == "3":
        level_three()
    else:
        print("Invalid choice. Please restart the program and select a valid level.")


shift_cipher()
