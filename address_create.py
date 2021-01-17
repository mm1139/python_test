import os
import ecdsa
import hashlib
import base58

private_key = os.urandom(32)
public_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key.to_string()

prefix_and_pubkey = b"\x04" + public_key

intermediate = hashlib.sha256(prefix_and_pubkey).digest()
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(intermediate)
hash160 = ripemd160.digest()
prefix_and_hash160 = b"\x00" + hash160

#hashlib.sha256が入れ子になっていることを確認
double_hash = hashlib.sha256(hashlib.sha256(prefix_and_hash160).digest()).digest()
checksum = double_hash[:4]
pre_address = prefix_and_hash160 + checksum

address = base58.b58encode(pre_address)
print(address.decode())