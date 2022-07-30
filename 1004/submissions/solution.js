const { createInterface } = require('readline');
const rl = createInterface({
    input: process.stdin,
    output: null
});

rl.question('', n => {
    rl.question('', nums => {
        var sum = 0;
        nums.split(' ').forEach(e => {sum += parseInt(e);});
        console.log(sum);
        rl.close();
    });
});