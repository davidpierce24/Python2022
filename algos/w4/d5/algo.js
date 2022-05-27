// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129

/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/
function binaryStringExpansion(str, solutions = [], partial = "") {
    const index = str.indexOf("?"); //indexOf returns the first string occurrence of a substring
  
    if (index < 0) {
      solutions.push(partial + str);
    } else {
      const front = str.slice(0, index); // Returns a section of the string
      const back = str.slice(index + 1); //Returns a section of the string
      const prefix = partial + front; //Slice of a string being processed
  
      binaryStringExpansion(back, solutions, prefix + "0"); //recursion
      binaryStringExpansion(back, solutions, prefix + "1"); //recursion
    }
    return solutions;
  }
  console.log(binaryStringExpansion("1?0?")) // ["1000", "1001", "1100", "1101"]