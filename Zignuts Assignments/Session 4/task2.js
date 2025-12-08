str = "1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"
let values = str.split(",")
console.log(typeof(values))
let sum=0;
for(i of values){
    sum+=Number(i);
}

console.log(sum)