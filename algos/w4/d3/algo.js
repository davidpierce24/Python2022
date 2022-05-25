    /* 
    Recursively reverse a string
    helpful methods:
    str.slice(beginIndex[, endIndex])
    returns a new string from beginIndex to endIndex exclusive
    */

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";
// console.log(str1.slice(str1[0], str1[1]))
var q = (str1.slice(0,1))
// console.log(q)

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) { 
    if(str.length == 0) {
        return ''
    }
    var mine = str.slice(1) 
    console.log(mine)
    var keep = str[0]
    console.log(keep)
    return reverseStr(mine) + keep
}

console.log(reverseStr('ghost'))

function rev(str){
    var a = str.split('')
    var b = []
    for(var i=str.length-1; i>=0; i--){
        b.push(str[i])
    }
    var c = b.join()
    var d = c.toString()
    return d
}

console.log(rev('dog'))