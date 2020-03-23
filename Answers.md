## Interview Questions

#1. Explain in detail the workings of a dynamic array:

Array is a sequence of elements of the same type stored in a contiguous block of memory. They're extremely time and space efficient.

Declaring an array

1. Determine how big array needs to be (each integer is 4 bytes)
2. Request block of memory that will fit the array
3. Receive the memory address of the reserved block of memory
4. Write values into the array

Find an index:
index \* sizeof(type) + start_address

#2. What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
Access an array = O(1), constant time.
Add or remove from front = O(n), linear. (have to move each element over an index one at a time)
Add or remove from back = O(1), constant time. sometimes O(n) if we call double size or resize, but we amortize (call it O(1) b/c more often than not thats what it is)

#3. What is the worse case scenario if you try to extend the storage size of a dynamic array?
O(n), since we would have to copy each element into the new space one at a time.

#4. Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
A typical block structure:
index number, timestamp, list of transactions, proof used to mine the block, hash of previous block.

The blocks are organized based off the order each one was mined. Each block has a hash of their previous block.

The chain is just the entire list of blocks all linked together and the respective data in each block.

#5. Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of work - artibtarily difficult problem that takes a large amount of computation to solve. Protects the blockchain by making it hard to make a new block.

Explanation:
Attackers could try to compromise the chain by altering the data in blocks to give it to themselves, among other possibilites.
However, the chain of hashes will break (a block's hash won't be identical to the next block in the chain's previous hash) and we will know that it is invalid.
Attackers would have to change the entire chain, not just a block, to make all of the hashes line up with the previous hashes.
Proof of work prevents the attackers from doing this. The only way the attacker could get their chain approved is if it was the longest chain (since longest chain wins), but the only way for the attacker to do this would be to take over half of all machines actively mining.
