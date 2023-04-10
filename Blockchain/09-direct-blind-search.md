## Search & indexing by using Cryptography
This is a search algorithm for searching in a "dictionary" to find the same results. The search keyword must encrypting by sha-256, 
because the dictionary key's are sha-256. The search results show in an array.

#### The example code by JavaScript:

```javascript
const crypto = require('crypto'); // import the built-in crypto module for hashing

function searchDictionary(keyword, dictionary) {
	const hashedKeyword = crypto.createHash('sha256').update(keyword).digest('hex'); // hash the keyword using sha-256
	const results = [];
	for (const key in dictionary) {
		if (key === hashedKeyword) {
			// add the value to the results array if the hashed key matches the hashed keyword
			results.push(dictionary[key]); 
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
#

#### Another example in Javascript:
```js
// Function to hash a keyword using SHA-256 algorithm
function hashKeyword(keyword) {
	let hashedKeyword = sha256(keyword);
	return hashedKeyword;
}

// Function to hash full content using a hashed keyword as key for cipher and decipher
function hashContent(keyword, content) {
	let hashedKeyword = hashKeyword(keyword);
	let cipher = CryptoJS.AES.encrypt(content, hashedKeyword);
	let hashedContent = sha256(cipher.toString());
	return hashedContent;
}

// Function to create a dictionary of hashed keywords and their corresponding hashed content
function createHashedKeywordsDictionary(keywords, contents) {
	let dictionary = {};
	for (let i = 0; i < keywords.length; i++) {
	let hashedKeyword = hashKeyword(keywords[i]);
	let hashedContent = hashContent(keywords[i], contents[i]);
	dictionary[hashedKeyword] = hashedContent;
}
return dictionary;
}

// Sample usage
let keywords = ['important', 'keywords'];
let contents = ['This document contains important information.', 'Use these keywords to find what you are looking for.'];
let dictionary = createHashedKeywordsDictionary(keywords, contents);
let searchedKeyword = 'important';
let hashedSearchedKeyword = hashKeyword(searchedKeyword);
let results = dictionary[hashedSearchedKeyword];
console.log(results);
```

### This example not complete but preseting:
- 1- keep the documents have included important keywords
- 2- hash the keyword (sha-256)
- 3- hash the full content of that keyword, by using "hashed keyword" as key for cipher & decipher
- 4- make a map(dictionary) the key is "keyword hash" and value is "the hash of contents have the keyword as a part of content included"
- 5- after search keyword:
	- 5-1- hash the searched keyword
	- 5-2- search and compaire the database of hashed keywords (dictionary)
	- 5-3- return results with same hash

"Javascript codes use built-in nodejs"
