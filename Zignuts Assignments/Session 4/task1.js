let inp = "foo8bar8cat2tc2"

let sum=0
for(i of inp){
    if(!isNaN(i))
        sum+=Number(i)
}

console.log(sum)