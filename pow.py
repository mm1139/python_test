import hashlib

class Block():
    def __init__(self, data, prev_hash):
        self.index = 0
        self.nonce = 0
        self.prev_hash = prev_hash
        self.data = data

    def blockhash(self):
        blockheader = str(self.index) + str(self.prev_hash) + str(self.data) + str(self.nonce)
        block_hash = hashlib.sha256(blockheader.encode()).hexdigest()
        return block_hash
    
    def __str__(self):
        return "Block Hash:" + self.blockhash() + "\nPrevious Hash:" + self.prev_hash + "\nindex:" + str(self.index) + "\nNonce:" + str(self.nonce) + "\n----------"
    

class Hashchain():
    def __init__(self):
        self.chain = ["000000000000000000000000000000000000000000000000000000"]
    
    def add(self, hash):
        self.chain.append(hash)
    

hashchain = Hashchain()
target = 0x777777 * 2**(8*(0x1e - 0x03))
for i in range(30):
    block = Block("Block " + str(i+1), hashchain.chain[-1])
    block.index = block.index + i + 1
    for n in range(4294967296):
        block.nonce = block.nonce + n
        if int(block.blockhash(), 16) < target:
            print(block)
            hashchain.add(block.blockhash())
            break
