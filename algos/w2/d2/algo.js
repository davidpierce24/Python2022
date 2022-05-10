/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

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

// These two do the same thing

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


/*******************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

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


/***********************************/

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

function reverseWordOrder(wordsStr) {
    var temp = wordsStr.split(" ")
    var final = ""
    console.log(temp)
    for(var j = temp.length -1; j>=0; j--){
        final += temp[j]
        final += " "
        console.log(final)
    }
    console.log(final)
}

reverseWordOrder(str1)