const readline = require('readline');

const name_input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

name_input.on('line', (input) => {
    console.log(`Your name is: ${input}`);
    rl.close();
});

name_input.on('close', () => {
    console.log('This important software is now closing');
    process.exit(0);
});
