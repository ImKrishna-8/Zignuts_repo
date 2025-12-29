inp = document.getElementById("inp");
out = document.getElementById("out");
btn = document.getElementsByTagName("button")[0]
head2 = document.getElementById("head")


btn.addEventListener("click", () => {
    
    let first_el = 0
    let second_el = 1
    let no_of_steps = Number(inp.value)

    head2.innerText = `Entered Number is ${no_of_steps} Fibonacci Series : `
    out.innerText = first_el + " " + second_el + " ";
    for (let i = 0; i < no_of_steps-2; i++) {
        let res = first_el + second_el;
        out.innerText =out.innerText+ res + " "
        first_el = second_el
        second_el = res
    }

    
})
