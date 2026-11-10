import string

cipher_hex = input("Enter your hex:")

cipher = bytes.fromhex(cipher_hex)

known_prefix = b"THM{"


key_prefix = bytes(
    cipher[i] ^ known_prefix[i]
    for i in range(len(known_prefix))
)

print("Recovered first four key bytes:", key_prefix)


charset = string.ascii_letters + string.digits

for fifth_char in charset:
    key = key_prefix + fifth_char.encode()

    plaintext = bytes(
        value ^ key[i % len(key)]
        for i, value in enumerate(cipher)
    )

    if (
        plaintext.startswith(b"THM{")
        and plaintext.endswith(b"}")
        and all(32 <= b <= 126 for b in plaintext)
    ):
        print("Possible key:", key.decode())
        print("Decoded text:", plaintext.decode())