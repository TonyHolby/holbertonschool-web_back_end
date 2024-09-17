const readline = require('readline');

const nameInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

nameInput.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  nameInput.close();
});

if (process.stdin.isTTY) {
  nameInput.on('close', () => {
    process.exit(0);
  });
} else {
  nameInput.on('close', () => {
    console.log('This important software is now closing');
    process.exit(0);
  });
}
