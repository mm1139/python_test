import requests


APIURL = "https://blockchain.info/rawtx/"
TXID = "b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da"

# r = requests.get(APIURL + TXID + "?format=hex")
r = requests.get(APIURL + TXID )
print(r.text)