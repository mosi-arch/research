## Search & indexing by using Cryptography
This is a search algorithm for searching in a "dictionary" to find the same results. The search keyword must encrypting by sha-256, 
because the dictionary key's are sha-256. The search results show in an array.\
The example code by JavaScript:

```javascript
const crypto = require('crypto'); // import the built-in crypto module for hashing

function searchDictionary(keyword, dictionary) {
	const hashedKeyword = crypto.createHash('sha256').update(keyword).digest('hex'); // hash the keyword using sha-256
	const results = [];
	for (const key in dictionary) {
		if (key === hashedKeyword) {
			results.push(dictionary[key]); // add the value to the results array if the hashed key matches the hashed keyword
		}
	}
	return results;
}

// example usage
// "key" the hash of keyword, but in "value" can replace whole of a text plain (content, link address, pdf, etc...) or another
// hash, that present the content, the key for that hash would be the key of dictionary.
const dictionary = {
	'fca5e2d5d5f5c2ef2b7c5d9b302f7d88da5c15f1f1e546c708b7e8516aafbab1': 'apple', 
	'9a7d1e50f8d4e4b4c8b7f4f3c3e7d3b2d9b7f3c5f0b7e5f8e8d7c7d9a8b2f2': 'banana',
	'0f8ad3d7d7f5c5ef7b2c9d9b7f7e5c1d7a5b1f1f1e5b6c4d7b2f5f9e5e1d2': 'orange',
};

const results = searchDictionary('apple', dictionary); // returns ['apple']
```
