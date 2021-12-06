from urllib.request import hashlib


upperbound = 0x0000000000000000000ffdd712a852e0d4234e6b

id = "balisarra"

for x in range(1, 1000000000):
    maybe_as_str = id+str(x)
    maybe_as_hex = int(hashlib.sha1(
        bytes(maybe_as_str, 'utf-8')).hexdigest(), 16)
    print(maybe_as_str)
    if maybe_as_hex <= upperbound:
        print("found it it is ", maybe_as_str)
        quit()