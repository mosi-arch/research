const crypto = require('crypto');

// Encryption function
function encrypt(text, key, iv) {
  const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

// Decryption function
function decrypt(encryptedText, key, iv) {
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

// Example usage
const text = 'Hello, World!';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

const encryptedText = encrypt(text, key, iv);
console.log('Encrypted Text:', encryptedText);

const decryptedText = decrypt(encryptedText, key, iv);
console.log('Decrypted Text:', decryptedText);
