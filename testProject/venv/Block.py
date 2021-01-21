import hashlib as ha

class Block:
    def __init__(self, index, transactions, blockTimeStamp, previousHash):
        self.index = index
        self.transactions = transactions
        self.blockTimeStamp = blockTimeStamp
        self.previousHash = previousHash
        self.nonce = 0


    def computeTheHashCode(self):
        #print("computeTheHashCode method")
        #print(self.previousHash)
        stringToBeManipulated ="".join(self.transactions) + self.previousHash
        objHash =  ha.sha256(stringToBeManipulated.encode()).hexdigest()
        #print('the block hashcode: '+ objHash)
        return objHash
