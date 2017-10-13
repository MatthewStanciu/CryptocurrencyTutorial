import os
import ecdsa

# Generate a random private key. This will be different every time you run
# the program.
private_key = os.urandom(32).encode('hex')
print ("Private key: " + private_key)

# The signing key - derived from the private key using the ECDSA algorithm
# Used for digital signatures. Still a private key
sk = ecdsa.SigningKey.from_string(private_key.decode('hex'), curve=ecdsa.SECP256k1)
# A public key used to verify that you did in fact sign the document
vk = sk.verifying_key

# The verifying key is not in the format that Bitcoin uses, so, per the
# Bitcoin docs, another byte, 04, is added to the beginning of the verifying key
# to create the public key.
public_key = ('\04'+vk.to_string()).encode('hex')
print "Public key: " + public_key

# Example use case
# When verifying, you send a recipient 3 things: your verifying key,
# the original message, and the signed message
msg = "hello world"
signed_msg = sk.sign(msg)
print signed_msg.encode('hex')

# The recipient can then use your verifying key to verify that your message is
# legitimate and was signed using your and only your signature key
assert vk.verify(signed_msg, "hello world")
