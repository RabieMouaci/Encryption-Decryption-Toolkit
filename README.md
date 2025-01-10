# Multi-Level Cipher Project

## Overview
This project implements a multi-level ciphering and deciphering system in Python. Users can choose between three levels of encryption and decryption, ranging from a simple shift cipher to a more complex hybrid cipher combining Vigenère and columnar transposition techniques.

## Features
### Level 1: Basic Shift Cipher
- Simple Caesar cipher with a user-defined shift.
- Encrypts alphabetic characters while leaving spaces and punctuation unchanged.

### Level 2: Vigenère Cipher
- Encrypts messages using a keyword-based polyalphabetic substitution.
- Supports case sensitivity and leaves non-alphabetic characters unchanged.

### Level 3: Hybrid Cipher
- Combines the Vigenère cipher with a columnar transposition cipher.
- Requires both a keyword (for Vigenère) and a numeric key (for columnar transposition).

## Usage
### Encryption
1. Run the encryption script.
2. Select the desired level (1, 2, or 3).
3. Provide the required inputs:
   - Level 1: Shift value.
   - Level 2: Keyword.
   - Level 3: Keyword (for Vigenère) and numeric key (for columnar transposition).
4. Enter the message to encrypt.
5. Receive the encrypted output.

### Decryption
1. Run the decryption script.
2. Select the appropriate level (1, 2, or 3).
3. Provide the same inputs (shift value, keyword, numeric key) used during encryption.
4. Enter the encrypted message.
5. Receive the original message as output.




