### Solution algorithm for finding targeted data in a pool of data without revealing the whole document:

1. **Define the targeted data**:\
	Determine what specific data needs to be found in the pool of data.

2. **Hash the targeted data**:\
	Use a cryptographic hash function to generate a unique fixed-size representation of the targeted data. This hashed value will be used to search for the targeted data without revealing the actual data.

3. **Hash the pool of data**:\
	Hash all of the data in the pool using the same cryptographic hash function. This will generate hashed values for all of the data in the pool.

4. **Compare the hashed values**:\
	Search through the hashed values for a match with the hashed value of the targeted data. If a match is found, the original data can be retrieved from the pool of data without revealing the other data in the pool.

5. **Repeat the process**:\
	If the targeted data is not found in the pool of data, repeat steps 1-4 with a new set of data.

### Mathematics formula:

The mathematical formula used in this algorithm is the cryptographic hash function, which takes any input data and produces a fixed-size output known as a hash value. This function is denoted as:

`H(x) = y`

Where `x` is the input data, `H` is the hash function, and `y` is the resulting hash value.

#

- Python example simulation:

```python
import hashlib

# Define the targeted data
target_data = "secret message"

# Hash the targeted data
target_hash = hashlib.sha256(target_data.encode()).hexdigest()

# Hash the pool of data
pool_data = ["random data 1", "secret message", "random data 2"]
pool_hashes = [hashlib.sha256(data.encode()).hexdigest() for data in pool_data]

# Compare the hashed values
if target_hash in pool_hashes:
    index = pool_hashes.index(target_hash)
    print("Targeted data found:", pool_data[index])
else:
    print("Targeted data not found")
```

- First hashes the targeted data using the SHA-256 cryptographic hash function. 
- It then hashes each item in the pool of data and stores these hashed values in a list. 
- The code then compares the hashed value of the targeted data with the hashed values in the pool. 
- If there is a match, the original data is retrieved from the pool. 
- Otherwise, the code prints a message indicating that the targeted data was not found.

---

#### The time complexity of the algorithm:
The time complexity of the algorithm for finding targeted data in a pool of data depends on the size of the pool and the hashing algorithm used. 

In the example algorithm I provided, the time complexity of hashing the targeted data and the pool of data is O(n), where n is the number of items in the pool. The time complexity of searching for a match in the hashed values is also O(n) in the worst case, where the targeted data is not in the pool.

If a more efficient hashing algorithm is used, such as SHA-512 or BLAKE2, the time complexity can be reduced to O(log n) or even O(1) for very large pools of data.

Finally, the time complexity of the algorithm depends on the specific implementation and the size of the data pool, but it is generally efficient for moderate-sized data pools.

#### Solution for saving time:
When save database, a version or the data saved by hash. Then search algorithm have less time.
