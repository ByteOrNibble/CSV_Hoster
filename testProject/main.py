import hashlib as ha
import time as t
import datetime as dt
import pandas as pd

from builtins import print
from timeit import default_timer as timer

from Block import Block
from BlockChain import BlockChain


print('Beginning Testing Hashing Capabilities')

message = 'hello world'
hashOfMessage = ha.sha256(message.encode()).hexdigest()

print(message)
print(hashOfMessage)
print('Ending Testing for Hashing Capabilities')

message2 = 'hello world!'
hashOfMessage2 = ha.sha256(message2.encode()).hexdigest();
different = False


print('Testing if the hash of message 1 and the hash of message 2 are the same with a singular character difference')
print('Message 1: '+message)
print(hashOfMessage)
print('Message 2: ' + message2)
print(hashOfMessage2)

if hashOfMessage != hashOfMessage2:
    different = True

print('Value of the test working out if there is a difference in the hashed values: ' + different.__str__())
print('Ending Testing of if the hash of message 1 and the hash of message 2 are the same with a singular character difference')

time1 = t.time()
datTime = dt.time()
start = timer()
print('here we go')
end = timer()
datTime2 = dt.time()
print('Difference between the timer ' + (end - start).__str__())
t.sleep(1)
time2 = t.time()
timeDif = time2 - time1
print(time1)
print(time2)
print("time diference with time suite: " + (t.time() - time1).__str__())

print('Creating genesis block prototype')
genesisBlockExample = Block(0, [], t.time(), "Genesis Block Message in the previous Hash's param space")
print('Block instantiated')
genesisBlockExample.computeTheHashCode();

print('Begin instantiating the Blockchain itself, set up to create the genesis block on call')
blockchain = BlockChain();
addNewBlockTest = Block(1, [], t.time(), blockchain.lastBlockInTheChain)
addNewBlockTest.computeTheHashCode()
blockchain.addABlockToTheChain(addNewBlockTest, "Dr No MD")

print('Previous Hashcode Was: ' + str(blockchain.lastBlockInTheChain))
addNewBlockTest = Block(2, [], t.time(), blockchain.lastBlockInTheChain)
addNewBlockTest = Block(3, [], t.time(), blockchain.lastBlockInTheChain)
blockchain.addABlockToTheChain(addNewBlockTest, "Dr No MD")
print('Add New Block Test Has Been Completed')

print('Beginning the importing of the csv from data.world which we will populate our bockchains arbitrary data with')
data = pd.read_csv("https://raw.githubusercontent.com/ByteOrNibble/CSV_Hoster/main/2020_GB_Region_Mobility_Report.csv")
print("Completed import of data from git hub host repository")
print(data.size)
print(data.head(5))
dates = data[["country_region", "date"]]
print(dates.head(10).shape)
print(dates.head(10))
print(dates.index)
print("number of rows"+ str(len(dates.index)))
top10 = dates.head(10).transpose()
top100 = dates.head(100).transpose()
top1000 = dates.head(1000).transpose()
top10000 = dates.head(10000).transpose()
top100000 = dates.head(100000).transpose()
top1000000 = dates.head(1000000).transpose()

print("Starting a new Blockchain to measure the performance from scratch")
performanceBlockChain = BlockChain()
count = 1
print(dates.size)
timerFor10Start = dt.datetime.now()
for x in top10:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor10End = dt.datetime.now()
print("total elapsed time for 10 records")
time_diff = (timerfor10End - timerFor10Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)

timerFor100Start = dt.datetime.now()
for x in top100:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor100End = dt.datetime.now()
print("total elapsed time for 100 records")
time_diff = (timerfor100End - timerFor100Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)

timerFor1000Start = dt.datetime.now()
for x in top1000:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor1000End = dt.datetime.now()
print("total elapsed time for 1,000 records")
time_diff = (timerfor1000End - timerFor1000Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)

timerFor10000Start = dt.datetime.now()
for x in top10000:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor10000End = dt.datetime.now()
print("total elapsed time for 10,000 records")
time_diff = (timerfor10000End - timerFor10000Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)

timerFor100000Start = dt.datetime.now()
for x in top100000:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor100000End = dt.datetime.now()
print("total elapsed time for 100,000 records")
time_diff = (timerfor100000End - timerFor100000Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)

timerFor1000000Start = dt.datetime.now()
for x in top1000000:

    nextBlock = Block(count, ["Doctor says take one prozac"], t.time(), performanceBlockChain.lastBlockInTheChain)
    performanceBlockChain.addABlockToTheChain(nextBlock, "Dr No MD")
timerfor1000000End = dt.datetime.now()
print("total elapsed time for 1,000,000 records")
time_diff = (timerfor1000000End - timerFor1000000Start)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)