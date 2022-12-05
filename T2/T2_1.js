console.log("Example to read line by line text");
const f = require('fs');
const readline = require('readline');
var user_file = './T2_input2.txt';
var r = readline.createInterface({
    input : f.createReadStream(user_file)
});

/*
    A = rock    = 1
    B = paper   = 2
    C = scissor = 3

    X = rock    = 1
    Y = paper   = 2
    Z = scissor = 3

*/

// R > S > P > R
/**
 * A X == 6
 * A Y == 1 2
 * A Z == 1 3  
 */ 
elves_values = {A: 1, B: 2, C: 3}
my_values = {X: 1, Y: 2, Z: 3}

let win = 0

r.on('line', function (text) {

    //if(text[0] == A && text[2] == X  )
    //elf rock - me paper
    if((elves_values[text[0]] < my_values[text[2]]) || (elves_values[text[0]] === 3 && my_values[text[2]] === 1)){
        if(!(elves_values[text[0]] === 1 && my_values[text[2]] === 3)){
            win = win + 6 + my_values[text[2]]
        }
        //console.log("gane con papel a roca")
        else {
            win = win + 0 + my_values[text[2]]
        }
    }

    else{

        if(elves_values[text[0]] === my_values[text[2]]){
            win = win + 3 + my_values[text[2]]
            //console.log("empate")
        }

        else{
            win = win + my_values[text[2]]
        }
    }
/*
    if(!(elves_values[text[0]] < my_values[text[2]])){
        console.log("??")
    }
*/


    //console.log("a" + text);
    console.log(win)
    
});

