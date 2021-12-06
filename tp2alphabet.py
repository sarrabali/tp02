from urllib.request import hashlib
from itertools import  product
from string import ascii_letters

sha1hash = 0x0000000000000000000ffdd712a852e0d4234e6b

id = "balisara"

#for x in range(100000000-1,1000000000):
for x in product(ascii_letters,repeat=10):
    guess = id+ ''.join(x)
    hashedGuess = int(hashlib.sha1(bytes(guess, 'utf-8')).hexdigest(), 16)
    print(guess, end='')
    if hashedGuess <= sha1hash:
        print("The password is ", str(guess))
        quit()