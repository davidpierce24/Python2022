function recursiveFactorial(input) {
    if(input <=1){
      return 1
    }
    else{
    return(input * recursiveFactorial(input-1))
    }
  }




// 5 * 4 * 3 * 2 * 1
// 4 * 3 * 2 * 1
// 3 * 2 * 1


// console.log(recursiveFactorial(5))


// 5(4(3(2(1))))