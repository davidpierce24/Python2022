/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";

function rotateStr(str, amnt) {
    // amnt = str.length%amnt
    var x = str.length-amnt
    if(str.length < amnt){
        x = str.length - amnt%str.length
    }
    str = str.slice(x) + str.slice(0, x)

    console.log(str)
}

rotateStr(str,3)

/*****************************************************************************/
/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const expect1 = true;

const strA2 = "ABCD";
const strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const expect2 = false;

const strA3 = "ABCD";
const strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const expect3 = false;


function isRotation(s1, s2) {
    if(s1 !== s2 || s1.length != s2.length){
        return false
    }
    for(var i = 0; i<s1.length; i++){
        // var str = ""
        var str = s1.slice(i) + s1.slice(0, i)
        if(str == s2){
            return true
        }
    }
    return false
}

console.log(isRotation(strA1,strB1))

