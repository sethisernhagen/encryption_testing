#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 1fc6205fa5c73aa5abe0bfcb1933d3ee31b0ba70de5ddcee4b8ec42fec11fa236ceeaef4b134b446b4f17fac2b4eaba374cdcd16e7c90e7e3789c5309da5d9d7d459cc67dac9314d5ad086e26c407fdb
# d0b95c0ba9cea1d9a3d469dc751aee7d431bc7e791e2cca73a148686df32dadfe5b280f035bf934432a84e21eda2437d
# github reply+00651e6077be3878bdeac9a1aaca274225e9134c8d5f004a92cf000000011592170d92a169ce0eac3914
# tested gAAAAABZg7RuoNV7wAMLCw4KupxhQILv6H50blmmMZZmyQ06qNhqd5MZCe1XAzBL92lukwgifIZ2gng-0Lr_LB66s2ftDlxGfrUPllrvLupLFxv5tX1k_A=-97
# xXWX+q7TDXGbjJmtXy7RGrZYaphLz0W77hXT9t+9dLk='b'fZ79zoYrqNZRpItdRTilIg==

# reply+O8kT5ctk6YGq4ln6fsPinWxaaDYAh+od53LfNnpdpow=6FiLXAHsd7+n7iTqtCP5YA==@chat.globality.com
# https://juvenal.dev.globality.io/api/v2/company?name=Seth%20123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# https://juvenal.dev.globality.io/api/v2/company/reply+O8kT5ctk6YGq4ln6fsPinWxaaDYAh+od53LfNnpdpow=6FiLXAHsd7+n7iTqtCP5YA==@chat.globality.com
def main():
    email = b"1b574a80-54c4-897d-8057-5bacc4b844e8000000000000"
    email2 = b"1b574a80-54c4-897d-8057-5bacc4b844e8.03ef77cc-0ceb-4a10-9e96-e4f4e02347d60000000"
    key = os.urandom(32)
    key = b"12345678901234567890123456789012"
    print(len(key))
    iv = os.urandom(16)

    fernet_token = get_fernet_token()
    aes_token = get_aes_token(key, iv, email)
    aes_token_string = convert_aes_token(aes_token)
    print("Fernet Token \n{}".format(fernet_token))
    print("Fernet Token String\n{}".format(convert_fernet_token(fernet_token)))
    print("AES Token \n{}".format(aes_token))
    print("AES Token String\n{}".format(aes_token_string))
    print("Decrypted AES Token String\n{}".format(decrypt(aes_token_string, key, iv)))


def get_fernet_token():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"my deep dark secret")
    return token


def get_aes_token(key, iv, email):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(email) + encryptor.finalize()
    return ct


def convert_aes_token(token):
    return token.hex()


def convert_fernet_token(token):
    # return token.decode("utf-8")
    print("a=", token.hex())
    print("b=", token)
    return token.hex()


def decrypt(token, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    token_bytes = bytes.fromhex(token)
    return decryptor.update(token_bytes) + decryptor.finalize()

if __name__ == '__main__':
    main()
