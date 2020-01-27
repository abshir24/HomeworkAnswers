//The function accepts a number and a power
function power(num,exponent){
    //this returnValue variable stores the value of 
    // num^exponent
    var returnValue = Math.pow(num,exponent)

    //return that value
    return returnValue
}

console.log(power(2,2))//this should print out 4


//the random number value prints X amount of random
//based on the input
function randomNumbers(value){
    var randomNumber;
    for(let i = 1;i<=value;i++){
        randomNumber = (Math.random()*100)+1
        console.log(randomNumber)
    }
}

randomNumbers(3)//this should print 3 random numbers to your console.