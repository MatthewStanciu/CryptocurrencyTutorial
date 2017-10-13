import hashlib
import os
import ecdsa
import base58

# Generate a public/private keypair - see the other file for how this works
private_key = os.urandom(32).encode('hex')
print ("Private key: " + private_key)
sk = ecdsa.SigningKey.from_string(private_key.decode('hex'), curve=ecdsa.SECP256k1)
vk = sk.verifying_key
public_key = ('\04'+vk.to_string()).encode('hex')
print "\nPublic key: " + public_key

# Create a new ripemd160 hash
ripemd160 = hashlib.new('ripemd160')
# Update basically means to perform the actual hash function
ripemd160.update(hashlib.sha256(public_key.decode('hex')).digest())
# This is the network ID byte for Bitcoin's main network
middleman = '\00' + ripemd160.digest()
# The checksum is the first 4 bytes of a double hash of the middleman
checksum = hashlib.sha256(hashlib.sha256(middleman).digest()).digest()[:4]
# Finally, add your middleman and checksum together and base58 encode it
# Base58 is like Base64 but without characters such as 0,o,l,I, etc.
address = base58.b58encode(middleman + checksum)

print "\nWallet address: " + address + "\n"
# You can verify that you did it correctly by visiting
# www.bitaddress.org & clicking on "Wallet Details" and
# typing your private key
