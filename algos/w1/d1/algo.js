function rotateArray(arr, shiftBy) {
    var lastItem = arr[arr.length - 1];
    for (var i=arr.length - 1; i>=0; i--) {
        arr[i] = arr[i-shiftBy];    
    }
    arr[0] = lastItem;
    return arr;
}

console.log(rotateArray([1,2,3,4,5], 2));