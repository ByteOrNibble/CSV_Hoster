from Block import Block
import time as t
import hashlib as ha

class BlockChain:

    def __init__(self):
        self.unconfirmedTransactions = []
        self.chain = []
        self.createGenesisBlock()

    def createGenesisBlock(self):

        # using the results of the previous testing we are going to use this method to instantiate the
        # genesis block by defining the method in the blockchain class and task to run on instantion of a blockchain
        # object
        genesisBlock = Block(0, [], t.time(), "Genesis Block Message but .different to show in logs")
        print('Genesis Blocks Hashcode: ' + genesisBlock.computeTheHashCode())
        self.chain.append(genesisBlock.computeTheHashCode())

    @property
    def lastBlockInTheChain(self):
        return self.chain[-1]

    def addABlockToTheChain(self, block, verification):
        print('about to call previous hash')
        previousHash = self.lastBlockInTheChain

        # confirming that the previous item has not been tampered with  by comparing the hashcodes of this and the last
        # block on the chain
        if previousHash != block.previousHash:
            print("The hashcode did not match the previous blocks hash")
            return False

        # Arbitrary value that we are going to set as the necessary credential to have for adding to chain permissions
        if verification != "Dr No MD":
            print('The Verification on who is submitting to the chain is not permitted')
            return False

        print("Previous Hashcode and Verification came back correct proceeding to add block to the chain")
        self.chain.append(block)
        return True
