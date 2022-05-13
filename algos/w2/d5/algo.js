
var str = 'oh Hhhhey'
var str4 = 'oheyhhhh'


var str1 = str.split(' ').join('')
var string = str1.toLowerCase()

var str2 = str4.split(' ').join('')
var string2 = str2.toLowerCase()

console.log(string)

ob1 = {
    // 'k': 2,
    // 'l': 3
}

ob2 = {
    // 'k': 2,
    // 'l': 3
}
// console.log(ob1['k'])

for (var i of string){
    if(!ob1[i]) {
        ob1[i] = 1
    }
    else {
        ob1[i] ++
    }
    console.log(ob1) 
}

for (var i of string){
    if(!ob2[i]) {
        ob2[i] = 1
    }
    else {
        ob2[i] ++
    }
    console.log(ob2) 
}

if(ob1 == ob2){
    console.log(true)
}
else{
    console.log(false)
}

// const s = s.replace(([^\w]/g,"")).toLowerCase()