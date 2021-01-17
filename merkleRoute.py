import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

class MerkleTree():
    def __init__(self, tx_list):
        self.tx_list = tx_list
    
    def calc_merkleroot(self):
        txs = self.tx_list
        if len(txs) == 1:
            return txs[0]
        while len(txs) > 1:
            if len(txs) % 2 == 1:
                txs.append(txs[-1])
            hashes = []
            for i in range(0,len(txs),2):
                hashes.append(sha256("".join(txs[i:i+2])))
            txs = hashes
        return txs[0]

if __name__ == "__main__":
    txs = []
    mt = MerkleTree(txs)
    print(mt.calc_merkleroot())