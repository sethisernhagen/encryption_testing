from base64 import urlsafe_b64decode, urlsafe_b64encode
from uuid import uuid4, UUID
from Crypto import Random
from Crypto.Cipher import AES

# reply+av9pjScRhChJafHAuhtlgAjjlnpyE1g0FtIpPFJ3A8A=zOzKR861KMkzg_VYn5zFZw==@chat.globality.com

cursor_id = uuid4()
print("cursor_id=", cursor_id)
cursor_id_hex = cursor_id.hex
key = "Z" * 16

iv = Random.new().read(AES.block_size)
aes = AES.new(key, AES.MODE_CBC, iv)
cyphertext = aes.encrypt(cursor_id_hex)
address = "reply+{}{}@chat.globality.com".format(
    urlsafe_b64encode(cyphertext).decode('utf-8'),
    urlsafe_b64encode(iv).decode('utf-8'),
)
print("address=", address)

aes = AES.new(key, AES.MODE_CBC, urlsafe_b64decode(address[50:74]))

cursor_id_hex_decrypted = aes.decrypt(urlsafe_b64decode(address[6:50]))
print("decrypted_hex=", cursor_id_hex_decrypted)
print("decrypted_cursor_id=", UUID(cursor_id_hex_decrypted.decode("utf-8")))
