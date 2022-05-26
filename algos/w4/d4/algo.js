/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12, 32, 45, 47, 49, 50, 53];
const searchNum2 = 5;
const expected2 = true;

// console.log(nums2.slice(nums2.length/2))

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
function binarySearch(sortedNums, searchNum) {
    var newArr
    var middle = Math.floor((sortedNums.length-1)/2)
    if(sortedNums.length == 0){
        return false
    }
    else if (sortedNums[middle] == searchNum){
        return true
    }
    else if (sortedNums[middle] < searchNum){
        newArr = sortedNums.slice(middle+1)
    }
    else{
        newArr = sortedNums.slice(0, middle)
    }
    console.log(middle)
    console.log(newArr)
    console.log
    return binarySearch(newArr, searchNum)
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))




// function binarySearchOther(sortedNums, searchNum, start, stop) {
//     var newArr
//     var beg
//     var end
//     var middle = Math.floor((sortedNums.length-1)/2)
//     if(sortedNums.length == 0){
//         return false
//     }
//     else if (sortedNums[middle] == searchNum){
//         return true
//     }
//     else if (sortedNums[middle] < searchNum){
//         // newArr = sortedNums.slice(middle+1)
//         beg = 
//     }
//     else{
//         newArr = sortedNums.slice(0, middle)
//     }
//     console.log(newArr.findIndex(middle))
//     console.log(middle)
//     console.log(newArr)
//     return binarySearch(newArr, searchNum)
// }

// console.log(binarySearch(nums1, searchNum1))
// console.log(binarySearch(nums2, searchNum2))
// console.log(binarySearch(nums3, searchNum3))

// [4, 5, 6, 8, 12, 32, 45, 47, 49, 50, 53];