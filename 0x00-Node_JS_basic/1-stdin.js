console.log('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
    let name = process.stdin.read();
    if (name) {
        process.stdout.write(`Your name is: ${name}`);
    }

}).on('end', () => {
    process.stdout.write('This important software is now closing');
});
