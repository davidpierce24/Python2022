function arrayMissOneMaker(input) {
        var arr = []
        for(var i=0; i <= input; i++){
            if(i == Math.floor(Math.random()* input)){
                continue
            }
            arr.push(i)
        }
    return (arr)
    }

console.log(arrayMissOneMaker(10));


function findMissingValue(input) {

    var lowest = input[0];
    var highest = input[0];
    var sum1 = 0;

    for (var i = 0; i < input.length; i++){
        if (input[i] < lowest){
        lowest = input[i];
        } else if (input[i] > highest){
        highest = input[i];
        }
        sum1 += input[i]
    }


    var sum2 = 0;
    for (var k = lowest; k <= highest; k++){
        sum2 += k;
    }

    return sum2 - sum1;
}

console.log(findMissingValue([0,1,2,3,4,5,7,8,9,10]))