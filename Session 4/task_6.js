function fact(n){
    if(n==0) return 0;
    if(n==1) return 1;
    return n*fact(n-1);
}

let inp = 5;

console.log(`Factorial of ${inp} is ${fact(inp)}`);