# CryptocurrencyTutorial
The purpose of this repository is to familiarize people with how the blockchain works and how to build your own cryptocurrency/blockchain
completely from scratch -- that means not on top of the Ethereum blockchain or something similar. This allows anyone who views this
repository to obtain a much deeper understanding of the technology that powers Bitcoin, Ethereum, etc. which allows you to be at the
forefront of this rapidly growing industry.

# Notes
1. This is not at all practical. If you really want to make your own cryptocurrency, Ethereum is the way to go unless you
are a computer scientist who has a brilliant idea that improves or expands upon current blockchain technologies. This is only for
educational purposes (also, it's super basic).

2. At the moment, almost all of the code can only be run on Python 2.x, but I am working on writing them for Python 3+.

3. I still do not fully understand elliptic curve cryptography (which is used for keygen+digital signatures) and I didn't want to write my
   own base58 encoding class, so I used Python's libraries, which must be installed before you can run these files.
   
   Simply run **pip install base58** and **pip install ecdsa** in your terminal to install the libraries I used.
   
   I will definitely make my own base58 encoder in the future, and I will probably make my own ECDSA class (but probably not because it's
   really complicated)

4. I made this as part of my high school club, CAT Club, in preparation for CodeDay Chicago in February, but this repository is public for anyone to stumble upon and learn more about the blockchain.
