entry_id = 0
class Entry {
    constructor(name, quantity, price) {
        this.id = entry_id;
        entry_id++;
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }
}

const newEntry = new Entry("nike", 100, 15);
console.log(newEntry.name);
console.log(newEntry.quantity);
console.log(newEntry.price);


function editClick(){
    console.log(newEntry.name);
    console.log(entry_id);
}


function deleteClick(){
    console.log("Trying to delete")
}