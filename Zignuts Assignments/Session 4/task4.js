class university{
    departments=[]
    constructor(u_name){
        this.u_name = u_name;
    }

    add_department(name){
        this.departments.push(name);
        console.log("Department Added !! ")
    }

    remove_department(name){
        for(let i=0;i<this.departments.length;i++){
            if(this.departments[i] == name){
                this.departments.splice(i,1)
                console.log("Department removed!")
                console.log("Remaining Departments:");
                this.show_departments()
                return;
            }
        }
        console.log("NO department Found!!")
    }

    show_departments(){
        this.departments.forEach(dept => {
            console.log(dept)
        });
    }
}

const GTU = new university("GTU");
GTU.add_department("IT"); 
GTU.add_department("CE"); 
GTU.add_department("ICT");
GTU.show_departments();
GTU.remove_department("ICT")

