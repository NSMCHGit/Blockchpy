from block import Block #importing the Block class  from block.py
import datetime 

block_chain = [Block.create_genesis_block()]  #the genesis block is created and stored in the list
print("The genesis block is created!")
print("Hash: %s" % block_chain[-1].hash) # hash of the genesis block

num_blocks_to_add = int(input('Enter the no.of blocks'))

# the for loop creates and prints the hashes of the 15 blocks in the respective chain order.
for i in range(1,num_blocks_to_add+1):
    block_chain.append(Block(block_chain[-1].hash,
                            "DATA!",
                            datetime.datetime.now()))
    print("Block %d has been created" %i)
    print("Block %d hash: %s"%(i,block_chain[-1].hash))
