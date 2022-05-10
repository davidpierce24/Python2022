/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

// const str1 = "abcABC";
// const expected1 = "abcABC";

// const str2 = "helloo";
// const expected2 = "helo";

// const str3 = "";
// const expected3 = "";

// const str4 = "aa";
// const expected4 = "a";

// /**
//  * De-dupes the given string.
//  * @param {string} str A string that may contain duplicates.
//  * @returns {string} The given string with any duplicate characters removed.
//  */
function stringDedupe(str) {
        var temp = ""
        for(var i of str) {
                // console.log(i)
                if(!temp.includes(i)){
                        // console.log(i)
                        temp += i
                    }
                }
                console.log(temp)
            }

function stringDedupe(str) {
    var temp = ""
    for(var i of str) {
        var match = 0
        for(var j of temp){
            if(i == j){
                match = 1
                    }
                // console.log(i)
            }
        if(match == 0)
            temp += i
            }
        console.log(temp)
}
// const str2 = "helloo";

// stringDedupe(str1)

// for(var str of arr) {
//     // check to see if the freqTable contains the str as a key (meaning we have or haven't accounted for it yet)
//     if (!freqTable[str]) {
//         // first occurrence found
//         freqTable[str] = 1;
//     } else {
//         // else if the element is already in the freqTable, then we just need to add 1
//         freqTable[str]++;
//     }

/*******************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

// const str1 = "hello";
// // const expected1 = "olleh";

// const str2 = "hello world";
// // const expected2 = "olleh dlrow";

// const str3 = "abc def ghi";
// const expected3 = "cba fed ihg";

// /**
//  * Reverses the letters in each words in the given space separated
//  * string of words. Does NOT reverse the order of the words themselves.
//  * @param {string} str Contains space separated words.
//  * @returns {string} The given string with each word's letters reversed.
//  */
function reverseWords(str) {
    var temp = str.split(" ")
    var final = ""
    for(var j = 0; j<temp.length; j++){
        for(var i=temp[j].length-1; i>=0; i--){
            final += temp[j][i]
        }
        final += " "
    }
    console.log(final)
}

// reverseWords(str3)
// var arr = str2.split(" ")
// console.log(arr)

/***********************************/

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
// const expected1 = "test a is This";

const str2 = "hello";
// const expected2 = "hello";

const str3 = "   This  is a   test  ";
// const expected3 = "test a is This";

// /**
//  * Reverses the order of the words but not the words themselves form the given
//  * string of space separated words.
//  * @param {string} wordsStr A string containing space separated words.
//  * @returns {string} The given string with the word order reversed but the words
//  *    themselves are not reversed.
//  */
function reverseWordOrder(wordsStr) {
    var temp = wordsStr.split(" ")
    var final = ""
    console.log(temp)
    for(var j = temp.length -1; j>=0; j--){
        if(temp[j] == ""){
            continue
        }
        final += temp[j]
        final += " "
        console.log(final)
    }
    console.log(final)
}

reverseWordOrder(str1)