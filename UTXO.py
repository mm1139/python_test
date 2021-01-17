import json
import requests

#address = "1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F"
address = "3FkenCiXpSLqD8L79intRNXUgjRoH9sjXa"

res = requests.get("https://blockchain.info/unspent?active=" + address)
#print(res.text)

utxo_list = json.loads(res.text)["unspent_outputs"]

print(str(len(utxo_list)) + "個のUTXOが見つかりました")
for utxo in utxo_list:
    print(utxo["tx_hash"] + ":" + str(utxo["value"]) + " satoshis" )