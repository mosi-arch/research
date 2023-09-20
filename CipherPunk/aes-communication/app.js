const crypto = require('crypto');
const readline = require('readline');

const algorithms = ['aes-256-cbc', 'aes-192-cbc', 'aes-128-cbc'];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Encrypt or Decrypt? (e/d): ', (choice) => {
  if (choice.toLowerCase() === 'e') {
    rl.question('Enter the text message: ', (message) => {
      rl.question('Enter the encryption key: ', (key) => {
        rl.question(`Choose an encryption algorithm (${algorithms.map((alg, index) => `${index + 1}. ${alg}`).join(', ')}): `, (algorithmIndex) => {
          const algorithm = algorithms[parseInt(algorithmIndex) - 1];
          if (!algorithm) {
            console.log('Invalid algorithm');
            rl.close();
            return;
          }

          const encryptedMessage = encrypt(message, key, algorithm);
          console.log(`\nEncrypted message: ${encryptedMessage}`);
          rl.close();
        });
      });
    });
  } else if (choice.toLowerCase() === 'd') {
    rl.question('Enter the encrypted message: ', (encryptedMessage) => {
      rl.question('Enter the encryption key: ', (key) => {
        rl.question(`Choose an encryption algorithm (${algorithms.map((alg, index) => `${index + 1}. ${alg}`).join(', ')}): `, (algorithmIndex) => {
          const algorithm = algorithms[parseInt(algorithmIndex) - 1];
          if (!algorithm) {
            console.log('Invalid algorithm');
            rl.close();
            return;
          }

          const decryptedMessage = decrypt(encryptedMessage, key, algorithm);
          console.log(`\nDecrypted message: ${decryptedMessage}`);
          rl.close();
        });
      });
    });
  } else {
    console.log('Invalid choice');
    rl.close();
  }
});

function encrypt(text, key, algorithm) {
  const cipher = crypto.createCipher(algorithm, key);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

function decrypt(encryptedText, key, algorithm) {
  const decipher = crypto.createDecipher(algorithm, key);
  let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}
