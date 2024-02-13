#!/usr/bin/node

let xStr = '';
if (parseInt(process.argv[2])){
    for(let i = 0; i < process.argv[2]; i++){
        for(let j = 0; j < process.argv[2]; j++){
            xStr += 'X';
        }
        console.log(xStr);
    }
}else{
    console.log('Missing size');
}
