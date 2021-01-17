import hashlib

input_text = "satoshi"

for nonce in range(20):
    input_data = input_text + str(nonce)
    hash = hashlib.sha256(input_data.encode("UTF-8")).hexdigest()
    print(input_data + " → " + hash)