import rsa

# Generate public and private keys
(public_key, private_key) = rsa.newkeys(502)

# Print the keys
print(f"Public key: (n={hex(public_key.n)}, e={hex(public_key.e)})")
print(f"Private key: (n={hex(private_key.n)}, d={hex(private_key.d)})")

# Encrypt a message
message = input("Enter a message: ")
encrypted = rsa.encrypt(message.encode(), public_key)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = rsa.decrypt(encrypted, private_key)
print(f"Decrypted: {decrypted.decode()}")
