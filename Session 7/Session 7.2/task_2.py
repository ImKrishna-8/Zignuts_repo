contacts = {}

def add_contact():
    name = input("Enter Name: ")
    mobile_no = input("Enter Mobile No(10 digit only): ")

    if(len(mobile_no)>10 or (mobile_no.isdigit==False)):
        print("invalid input")
        return
    
    state = input("Enter State: ")
    city = input("Enter city: ")

    contacts[name] = {
        "name" :name,
        "mn": mobile_no,
        "address" : {
            "state" : state,
            "city" : city
        }
    }

def view_contacts():
    for i in contacts:
        person = contacts[i]
        print("name: ",person["name"])
        print("mobile no: ",person["mn"])
        print("address: ",person["address"]["city"]," ,", person["address"]["state"])


add_contact()
view_contacts()