var fs = require('fs')
var stdinBuffer = fs.readFileSync(0);

start()

async function start(){
    console.log()
    let n = 
    n = parseInt(n)
    
    let line = await getline()
    let nums = line.split(' ').map(e => parseInt(e))

    let sum = 0
    for(var i=0; i<nums.length; ++i){
        sum += nums[i];
    }
    console.log(sum.toString());

    // process.exit();
    console.log('');
    // process.exit()
}


