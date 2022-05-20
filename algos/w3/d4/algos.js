function bookIndex(pages) {
  var arr = []
  for(var i in pages){
    if ((pages[i] - pages[i-1]) != 1 ){
      arr.push(pages[i])
    }
}
console.log(arr)
}

bookIndex([1,2,3,6,7,9,11,12, 13,17])




function bookIndex2(pages) {
  var arr = []
  for(var i in pages){
    if (pages[i]+1 != pages[i+1]){
      arr.push(pages[i])
    }
  }
  console.log(arr)
}

bookIndex2([1,2,3,6,7,9,11,12,13,17])




// function bookIndex2(pages) {
//   var arr = []
//   for(var i in pages){
//     if (pages[i]+1 != pages[i+1]){
//       arr.push(pages[i])
//     }
//   }
// console.log(arr)
// }

// bookIndex2([223, 224, 225,226,227,231,232,233])



// function bookIndex(pages) {
//   var arr = []
//   for(var i in pages){
//     if ((pages[i] - pages[i-1]) != 1 ){
//       arr.push(pages[i])
//     }
// }
// console.log(arr)
// }

// bookIndex([223, 224, 225,226,227,231,232,233])