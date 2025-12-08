class shape {
    area(){
        console.log("Area calculation");
    }
}

class circle extends shape{
    area(r){
        return 3.14*r*r;
    }
}

class triangle extends shape{
    area(b,h){
        return 0.5*b*h;
    }
}


let radius = 7;
let height = 5,base=8;

let circle1 = new circle();
console.log(`Area of circle is : ${circle1.area(radius)}`);
let triangle1 = new triangle();
console.log(`Area of Triangle is : ${triangle1.area(base,height)}`);
